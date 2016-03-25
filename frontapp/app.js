var React = require('react');
var ReactDOM = require('react-dom');
var Button = require('./amazebutton');
var BasicInfo = require('./component/BasicInfo');
var TodoApp = require('./todoapp')

// using an ES6 transpiler, like babel
import { Router, Route, Link, browserHistory } from 'react-router'

var NoMatch = function(){
	return <div> No Match     </div>
}

ReactDOM.render(
    <Router history={browserHistory}>
    <Route path="/" component={TodoApp}>
      <Route path="about" component={Button}/>
      <Route path="users" component={BasicInfo}/>
    </Route>
  </Router>, 
    document.getElementById('app')
);

