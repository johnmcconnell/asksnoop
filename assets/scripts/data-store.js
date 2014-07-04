BareKnuckleApp.Models = new Object();

BareKnuckleApp.Models.Comment = DS.Model.extend({
		id : DS.attr('attr'),
		updatedOn : DS.attr('date'), 
		username : DS.attr('string'),
		content : DS.attr('string')
});

BareKnuckleApp.Models.Tag = DS.Model.extend({
	id : DS.attr('string'),
	updatedOn : DS.attr('date'),
	value : DS.attr('string')
});

BareKnuckeApp.Models.Entry = DS.Model.extend({
	id : DS.attr('string'),
	updatedOn : DS.attr('date'),
	author : DS.attr('string'),
	title : DS.attr('string'),
	markup : DS.attr('string'),
	published : DS.attr('boolean'),
	tags : DS.hasMany('tag'),
	comments : DS.hasMany('comment')
});