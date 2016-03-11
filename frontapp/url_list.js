var base_url = 'http://127.0.0.1:5000/api/'
var url_list = {
	'probs' : {
		  name : 'probs'
		, url  : base_url + 'prob'
	},
	'causes' : {
		 name : 'causes'
		, url  : base_url + 'causes'
	},
	'measures' : {
		 name : 'measures'
		, url  : base_url + 'measures'
	}
}

module.exports = url_list;