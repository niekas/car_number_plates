import React, { Component } from 'react';
import Owner from './Owner';
import ErrorMessage from './ErrorMessage';


class OwnerTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      new_first_name: '',
      new_last_name: '',
      error_message: null
    };

    this.resetNewOwnerState = this.resetNewOwnerState.bind(this);
    this.handleFirstNameChange = this.handleFirstNameChange.bind(this);
    this.handleLastNameChange = this.handleLastNameChange.bind(this);
    this.handleCreate = this.handleCreate.bind(this);
  };

  resetNewOwnerState(event) {
    this.setState({new_first_name: '', new_last_name: ''});
  };

  handleFirstNameChange(event) {
    this.setState({new_first_name: event.target.value});
  };

  handleLastNameChange(event) {
    this.setState({new_last_name: event.target.value});
  };

  onDelete() {
    this.props.onOwnerDelete(this.props.owner_id);
  };

  handleCreate(event) {
    event.preventDefault();
    
    function handlePOSTResponse(resp) {
      if (resp.status != 201) {
        resp.json().then(json => {
          this.setState({'error_message': json[Object.keys(json)[0]]});
        })
      } else {
        this.setState({'error_message': null});
        resp.json().then(json => {
          var new_element = {
            owner_id: json['id'].toString(),
            first_name: this.state.new_first_name,
            last_name: this.state.new_last_name,
          };
          this.resetNewOwnerState();
          this.props.onOwnerCreate(new_element);
        });
      };

    };
    handlePOSTResponse = handlePOSTResponse.bind(this);

    fetch('/api/owners/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        first_name: this.state.new_first_name,
        last_name: this.state.new_last_name,
        number_plate: []
      })
    }).then(handlePOSTResponse).catch(function (err) {
    });
  };

  render() {
    return ([
      <tr>
        <td colspan="2">
          <form onSubmit={ this.handleCreate }>
            <ErrorMessage error_message={ this.state.error_message }/>
            <input type="text" size="12" placeholder="First name" value={ this.state.new_first_name } onChange={ this.handleFirstNameChange } />
            <input type="text" size="12" placeholder="Last name" value={ this.state.new_last_name } onChange={ this.handleLastNameChange } />
            <button type="submit"> Create </button>
          </form>
        </td>
      </tr>,
      this.props.owners.map(data => {
        return <Owner first_name={ data.first_name } last_name={ data.last_name } owner_id={ data.id }
            onOwnerChange={ this.props.onOwnerChange } onOwnerDelete={ this.props.onOwnerDelete }/>
    })]);
  }
};

export default OwnerTable;
