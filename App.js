import React,{Component} from 'react';

class App extends Component{
	constructor(){
		super();
		this.state = {
			firstName : '',
			lastName : '',
			style : {}
		};
		this.handleChange = this.handleChange.bind(this);
	};
	
	handleChange(event){
		const {name,value} = event.target;
		this.setState({
			[name] : value
		})
	};
	
	render(){
		return(
			<div>
				<form>
					<input style={this.state.firstName.length >= 10 ? {color:'red'} : {color:'green'}} type='text' value={this.state.firstName} name='firstName' placeholder='First Name' onChange={this.handleChange}/>
					<input style={this.state.lastName.length >= 10 ? {color:'red'} : {color:'green'}} type='text' value={this.state.lastName} name='lastName' placeholder='Last Name' onChange={this.handleChange}/>
				</form>
				<h1>{this.state.firstName} {this.state.lastName}</h1>
			</div>
		);
	};
};

export default App;
