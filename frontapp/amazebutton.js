var React = require('react');
var AMUIReact = require('amazeui-react');
var Button = AMUIReact.Button;

var buttons  = React.createClass({
    render: function(){
      return (
           <div> <Button amStyle="secondary">Default</Button>
           <Button amStyle="primary">dds</Button></div>
          );
    }

});

module.exports = buttons;