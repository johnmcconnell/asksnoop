/*
 * Initialize App in Ember.js
 * Author: John McConnell
 * 
 */
BareKnuckleApp = Ember.Application.create();

/*
 * #/journal-entries/journal-entry/:id
 */
BareKnuckleApp.Router.map(function() {
	this.resource('entries', function() {
		this.resource('entry', {
			path : ':id'
		});
		this.resource('public-entry', {
			path :'/pub/:id'
		});
	});
	this.resource('comments');
	this.resource('home');
	this.resource('about');
	this.resource('login');
	this.resource('sign-up');
});

BareKnuckleApp.ApplicationRoute = Ember.Route.extend({
    setupController : function(controller,model) {
		controller.set('user', model);
	},
	model : function() {
		return LifeSights.User.read();
	}
});

BareKnuckleApp.ApplicationController = Ember.Controller.extend({
	title : 'Bare Knuckle Coding',
	needs: [ 'entries' ],
	actions : {
		login : function() {
			var user = this.get('user');
			var ajax = function() {
				return LifeSights.User.login(user.username, user.password);
			}
			var errors = LifeSights.HandleAjax('#trans-alert', ajax, function(data){ return data.errors});
			if (errors == null) {
				this.transitionToRoute('entries');
			}
		},
		logout : function() {
			LifeSights.HandleAjax('#trans-alert', LifeSights.User.logout, function(data) {});
			this.set('user', LifeSights.User.model());
			this.transitionToRoute('entries');
		}
	}
});

BareKnuckleApp.IndexRoute = Ember.Route.extend({
    redirect: function() {
        this.transitionTo('entries');
    }
});

BareKnuckleApp.LoginRoute = Ember.Route.extend({
	renderTemplate: function() {
	    this.render({ controller: 'application' });
	}
});

BareKnuckleApp.LoginController = Ember.ObjectController.extend({
	needs: ['application']
});

BareKnuckleApp.EntriesRoute = Ember.Route.extend({
	setupController : function(controller, entries) {
		controller.set('model', entries);
	},
	model : function() {
		var data_handler = function(data) {
			return data.result;
		}
		return LifeSights.HandleAjax('#trans-alert',LifeSights.Entry.readAll,data_handler);
	}
});

BareKnuckleApp.EntriesController = Ember.ArrayController.extend({
	needs: ['application', 'entry'],
	actions : {
		addnew : function() {
			entry = LifeSights.Entry.model();
			this.pushObject(entry);
			this.transitionToRoute('entry', entry);
		}
	}
});

BareKnuckleApp.EntryRoute = Ember.Route.extend({
	setupController : function(controller, entry) {
		controller.set('model', entry);
	},
	model : function(params) {
		return BareKnuckle.EntriesController.findProperty('id', params.id);
	}
});

BareKnuckleApp.EntryController = Ember.ObjectController.extend({
	needs: [ 'entries'],
	isEditing : false,
	actions : {
		edit : function() {
			this.set('isEditing', true);
		},
		save : function() {
			var ajax_api = null;
			var data_handler = null
			var controller = this;
			var model = controller.get('model');
			
			if (model.id == 'new') {
				ajax_api = function() { return LifeSights.Entry.create(model); }
				data_handler = function(data) {
					if (data.success) {
						var entries_controller = controller.get('controllers.entries');
						// add, switch, remove
						entries_controller.pushObject(data.result[0]);
						controller.transitionToRoute('entry',data.result[0]);
						entries_controller.removeObject(controller.get('model'));
					}
				}
			} else {
				ajax_api = function() { return LifeSights.Entry.update(model); }
				data_handler = function(data) {}
			}
			
			LifeSights.HandleAjax('#trans-alert',ajax_api,data_handler);
			this.set('isEditing', false);
		},
		delete: function() {
			var model = this.get('model');
			var controller = this;
			if (model.id == 'new') {
				var entries_controller = controller.get('controllers.entries');
				entries_controller.removeObject(model);
			} else {
				var data_handler = function(data) {
					if (data.success) {
						var entries_controller = controller.get('controllers.entries');
						entries_controller.removeObject(model);
					}
				}
				ajax_api = function() { return LifeSights.Entry.delete(model); }
				LifeSights.HandleAjax('#trans-alert',ajax_api,data_handler);
			}
			this.transitionToRoute('entries');
			this.set('isEditing', false);
		},
		cancel : function() {
			this.set('isEditing', false);
		},
		addTag : function() {
			this.get('tags').pushObject(LifeSights.Tag.model());
		},
		deleteComment : function(comment) {
			var entry = this.get('model');
			var data_handler = function(data) {
				if (data.success) {
					entry.comments.removeObject(comment);
				}
			}
			ajax_api = function() { return LifeSights.Entry.deleteComment(entry,comment); }
			LifeSights.HandleAjax('#trans-alert',ajax_api,data_handler);
		}
	}
});

BareKnuckleApp.PublicEntryRoute = Ember.Route.extend({
	setupController : function(controller, entry) {
		controller.set('model', entry);
	},
	model : function(params) {
		return BareKnuckle.EntriesController.findProperty('id', params.id);
	}
});

BareKnuckleApp.PublicEntryController = Ember.ObjectController.extend({
	needs: ['application','entries'],
	actions : {
		reply : function(comment) {
			var username = this.get('controllers.application').get('user').username;
			if (!username) {
				username = "anonymous";
			}
			
			child = LifeSights.Comment.model();
			child.username = username;
			child.parentId = comment.id;
			child.edit = true;
			child.content = 'comment here';
			this.get('model').comments.pushObject(child);
		},
		save : function(comment) {
			var entry = this.get('model');
			var ajax_api = function() { return LifeSights.Entry.addComment(entry,comment) };
			LifeSights.HandleAjax('#trans-alert',ajax_api,function(data) {
				if (data.success) {
					entry.comments.removeObject(comment);
					comment.edit = false;
					entry.comments.addObject(comment);
				}
			});
			
		},
		cancel : function(comment) {
			this.get('model').comments.removeObject(comment);
		}
	}
});

BareKnuckleApp.CommentsRoute = Ember.Route.extend({
});

BareKnuckleApp.CommentsController = Ember.ArrayController.extend({
});

/*
 * Helper to print a timestamp as a nice date
 */
Ember.Handlebars.helper('pretty-date', function(timestamp) {
	var x = new Date(timestamp);
	return x.toDateString();
});

Ember.Handlebars.helper('format-markdown', function(data) {
	var converter = new Showdown.converter();
	return new Handlebars.SafeString(converter.makeHtml(data));
});

Ember.Handlebars.helper('format-comments', function(comments) {
	var dom = function(username, content) { 
		return $('<div>').text(username + ' says ' + content) }
	
	var root = comments.filterBy('parentId','root')[0];
	
	var toString = function(child) {
		if (!child) {
			return '';
		}
		children = comments.filterBy('parentId', child.id)
		
		var buff = ''
		for(var x = 0; x < children.length; x++) {
			var com = children[x];
			buff += dom(com.username, com.content).html();
			buff += toString(com);
		}
		
		return buff;
	}
	return toString(comments);
})

Handlebars.registerHelper('ifRoot', function(id, options) {
	console.log(id);
	if (id == 'parentId') {
		return options.fn(this);
	}
	return options.inverse(this);
});
