var React = require('react');
var reqwest = require('reqwest');


//- CommentBox
//  - CommentList
//    - Comment
//  - CommentForm


var Prob = React.createClass({
  render: function() {
    return (
      <div className="prob">
        {this.props.plv} : {this.props.children}
      </div>
    );
  }
});


var ProbList = React.createClass({
  render: function() {

  	var probNodes = this.props.data.map(function(prob) {
      return (
        <Prob plv={prob.PLV} key={prob.id}>
          {prob.PBC}
        </Prob>
      );
    });

    return (
      <div className="probList">
           {probNodes}
      </div>
    );
  }
});

var ProbForm = React.createClass({
  getInitialState: function() {
    return {plv: '', text: ''};
  },
  handlePlvChange: function(e) {
    this.setState({plv: e.target.value});
  },
  handleTextChange: function(e) {
    this.setState({text: e.target.value});
  },

  handleSubmit: function(e) {
    e.preventDefault();
    var plv = this.state.plv.trim();
    var text = this.state.text.trim();
    if (!text || !plv) {
      return;
    }
    // TODO: send request to the server
    this.props.onProbSubmit({plv: plv, text: text});
    this.setState({plv: '', text: ''});
  },

  render: function() {
    return (
      <form className="probForm" onSubmit={this.handleSubmit}>
        <input type="text" 
         placeholder="Your name" 
         value={this.state.plv}
         onChange={this.handlePlvChange} />
        <input type="text" 
         placeholder="Say something..." 
         value={this.state.text}
         onChange={this.handleTextChange}/>
        <input type="submit" value="Post" />
      </form>
    );
  }
});


var ProbBox = React.createClass({
  getInitialState: function() {
    return {data: []};
  },

  loadProbFromServer: function() {
    reqwest({
        url: 'http://127.0.0.1:5000/api/prob'
      , crossOrigin: true
      // , type: 'json'
      // , method: 'post'
      // , contentType: 'application/json'
      // , headers: {
      //     'X-My-Custom-Header': 'SomethingImportant'
      //   }
      , error: function (err) { 
          console.log(err);
      }
      , success: function (resp) {
          console.log(resp.data);
          this.setState({ data: resp.data });
        }.bind(this)
    });
  },

   componentDidMount: function() {
    this.loadProbFromServer();
    // setInterval(this.loadProbFromServer, this.props.pollInterval);
  },

  handleProbSubmit: function(prob) {
    // TODO: submit to the server and refresh the list
    reqwest({
      url: 'http://127.0.0.1:5000/api/prob/add'
      , type: 'json'
      , method: 'post'
      //, contentType: 'application/json'
      , crossOrigin: true
      , data: prob

      , success: function(resp) {
        this.setState({data: resp.data});
      }.bind(this)
      , error: function(err) {
        console.log(err);
      }
    });
  },

  render: function() {
    return (
      <div className="probBox">
        <h1>probs</h1>
        <ProbList data = {this.state.data}/>
        <ProbForm onProbSubmit={this.handleProbSubmit} />
      </div>
    );
  }
});

module.exports = ProbBox;