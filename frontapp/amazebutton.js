var React = require('react');

var AMUIReact = require('amazeui-react');
var reqwest = require('reqwest');
var Button = AMUIReact.Button;


var url_list = require('./url_list');

var ProbList = React.createClass({
  render: function(){

    var Nodes = this.props.data.map(function (node){
                  return (
                      <div key={node.id}>ID: {node.id}  PBC: {node.PBC}</div>
                  );
              });

    return (
          <div className="probList">
              {Nodes}
          </div>
      );
  }

});

var ProbForm = React.createClass({
  getInitialState: function(){
      return {KDNR: '', PBC: ''};
  },

  handleKDNRChange: function(e){
    this.setState({KDNR: e.target.value});
  },

  handlePBCChange: function(e){
    this.setState({PBC: e.target.value});
  },

  handleSubmit: function(e) {
    e.preventDefault();
    var KDNR = this.state.KDNR.trim();
    var PBC = this.state.PBC.trim();
    if (!KDNR || !PBC) {
      return;
    }
    // TODO: send request to the server
    this.props.onCommentSubmit({KDNR: KDNR, PBC: PBC});

    this.setState({KDNR: '', PBC: ''});
  },

  render: function(){
    return (
          <form onSubmit={this.handleSubmit}>
          <input
          type="text"
          placeholder="KDNR" 
          value={this.state.KDNR}
          onChange={this.handleKDNRChange}/>
        <input
          type="text"
          placeholder="PBC" 
          value={this.state.PBC}
          onChange={this.handlePBCChange}/>

          <input type="submit" value="Post" />
          </form>
      );
  }

});

var MainBoard  = React.createClass({

    getInitialState: function() {
        return {clicktimes: 0 ,data : []};
     },
/*
    componentDidMount: function() {
       reqwest({
            url: 'http://127.0.0.1:5000/api/prob'
          , crossOrigin: true
        }, function (resp) {
          if (this.isMounted()) {
            this.setState({
              data: resp.data,
              clicktimes: 20
            });
          }
        }.bind(this));
  },
*/  
    handleCommentSubmit: function(comment) {
      /*
      处理
      */
      var comments = this.state.data;
      var newComments = comments.concat([comment]);
      this.setState({data: newComments});
      console.log(comment);
    },

    handleClick: function(e) {
        e.preventDefault();
        console.log('click times:' + this.state.clicktimes);
        this.setState({clicktimes: this.state.clicktimes + 1});
        reqwest({
            url: url_list.probs.url
          , crossOrigin: true
        }, function (resp) {
            this.setState({
              data: resp.data,
            });
        }.bind(this));
    },

    render: function(){
      
      return (
           <div> 
           <Button onClick={this.handleClick}>Default</Button>
           <ProbList data={this.state.data}/>

           <ProbForm onCommentSubmit={this.handleCommentSubmit} />
           </div>
          );
    }

});

module.exports = MainBoard;