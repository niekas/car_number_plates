import React, { Component } from 'react';
import ErrorMessage from './ErrorMessage';


class Owner extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        error_message: null,
        editable: false
    };
    this.onFirstNameChange = this.onFirstNameChange.bind(this);
    this.handleLastNameChange = this.handleLastNameChange.bind(this);
    this.onDelete = this.onDelete.bind(this);
    this.toggleEditable = this.toggleEditable.bind(this);
  };

  onFirstNameChange(event) {
    this.props.onOwnerChange({
      id: this.props.owner_id,
      first_name: event.target.value,
      last_name: this.props.last_name,
    })
  };

  handleLastNameChange(event) {
    this.props.onOwnerChange({
      id: this.props.owner_id,
      first_name: this.props.first_name,
      last_name: event.target.value,
    })
  };

  toggleEditable(event) {
    if (this.state.editable === true) {
      function handlePATCHresponse(resp) {
        if (resp.status != 200) {
          resp.json().then(json => {
            this.setState({error_message: json[Object.keys(json)[0]]});
          })
        } else {
          this.setState({error_message: null, editable: false});
        };
      };
      handlePATCHresponse = handlePATCHresponse.bind(this);

      fetch('/api/owners/'+ this.props.owner_id + '/' , {
        method: 'PATCH',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'first_name': this.props.first_name,
          'last_name': this.props.last_name,
          'id': this.props.owner_id})
      }).then(handlePATCHresponse);
    } else {
      this.setState({editable: true});
    };
  };

  onDelete(event) {
    this.props.onOwnerDelete(this.props.owner_id);
  };

  render() {
    if (this.state.editable === true) {
      return (
        <tr>
          <td>
            <ErrorMessage error_message={ this.state.error_message }/>
            <input placeholder="First name" size="14" onChange={ this.onFirstNameChange } value={ this.props.first_name }/>
            <input placeholder="Last name" size="14" onChange={ this.handleLastNameChange } value={ this.props.last_name }/>
          </td>
          <td>
            <button type="button" onClick={ this.toggleEditable }> Save </button>
            <button type="button" onClick={ this.onDelete }> Delete </button>
          </td>
        </tr>
      );
    };
    return (
      <tr>
        <td>
          { this.props.first_name } { this.props.last_name }
        </td>
        <td>
          <button type="button" onClick={ this.toggleEditable }> Edit </button>
          <button type="button" onClick={ this.onDelete }> Delete </button>
        </td>
      </tr>
    );
  };
};

export default Owner;
