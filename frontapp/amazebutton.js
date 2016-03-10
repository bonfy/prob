var React = require('react');

var AMUIReact = require('amazeui-react');
var reqwest = require('reqwest');
var Button = AMUIReact.Button;


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
    handleClick: function(e) {
        e.preventDefault();
        console.log('click times:' + this.state.clicktimes);
        this.setState({clicktimes: this.state.clicktimes + 1});
        reqwest({
            url: 'http://127.0.0.1:5000/api/prob'
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
           </div>
          );
    }

});

module.exports = MainBoard;