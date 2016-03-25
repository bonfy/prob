var React = require('react');
var AMUIReact = require('amazeui-react');
var reqwest = require('reqwest');
var Container = AMUIReact.Container;
var Grid = AMUIReact.Grid;
var Col = AMUIReact.Col;

/* Model Type 组件*/
var Bon_ModelTyp = function(props){
	return 	<div>车型 Fzg.-Typ： {props.modell}</div>
}
/* Koodinator 组件*/
var Bon_Koodinator = (props) => {
	return <div>MQR协调 MQ-Koord.：{props.koodinator}</div>
}
/* KDNR 组件*/
var Bon_KDNR = React.createClass({

	render : function(){
		return (
			<div></div>
			);
	}
});

/* Lieferant： 组件*/

var Bon_Lieferant = (props) => {
	return <div>厂商 Lieferant： {props.lieferant}</div>
}

/* BasicInfo 组件*/
var BasicInfo = React.createClass({
	render : function(){

		return (
			 <div>
			    <Container>基本信息 Basisinformationen</Container>

			    <Grid className="doc-g">
			      <Col sm={6}><Bon_ModelTyp modell="Touran"/></Col>
			      <Col sm={6}><Bon_Koodinator koodinator="Touran"/></Col>

			      <Col sm={6}>KDNr：</Col>
			      <Col sm={6}><Bon_Lieferant lieferant="hello"/></Col>
			    </Grid>
    		  </div>
			);
	}
});

module.exports = BasicInfo;