import React, { Component } from 'react';
import NumberPlate from './NumberPlate';
import OwnerOptions from './OwnerOptions';
import ErrorMessage from './ErrorMessage';


class NumberPlateTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      new_number_plate: '',
      new_owner_id: -1,
      error_message: null
    };

    this.resetNewNumberPlateState = this.resetNewNumberPlateState.bind(this);
    this.handleOwnerChange = this.handleOwnerChange.bind(this);
    this.handleNumberPlateChange = this.handleNumberPlateChange.bind(this);
    this.handleCreate = this.handleCreate.bind(this);
  };

  resetNewNumberPlateState() {
    this.setState({new_number_plate: '', new_owner_id: -1, new_owner_full_name: '', error_message: null});
  };

  handleOwnerChange(event) {
    var owner_full_name = '';
    for (var i=0; i < this.props.owners.length; i++) {
      if (this.props.owners[i].id.toString() === event.target.value.toString()) {
        owner_full_name = this.props.owners[i].first_name + ' ' + this.props.owners[i].last_name;
        break;
      };
    };
    this.setState({new_owner_id: event.target.value, new_owner_full_name: owner_full_name});
  };

  handleNumberPlateChange(event) {
    this.setState({new_number_plate: event.target.value});
  };

  handleCreate(event) {
    event.preventDefault();
    function handlePOSTResponse(resp) {
      if (resp.status !== 201) {
        resp.json().then(json => {
          this.setState({'error_message': json[Object.keys(json)[0]]});
        })
      } else {
        resp.json().then(json => {
          var new_element = {
            owner: this.state.new_owner_id,
            owner_full_name: this.state.new_owner_full_name,
            number: this.state.new_number_plate,
            id: json['id']
          };
          this.props.onNumberPlateCreate(new_element);
          this.resetNewNumberPlateState();
        });
      };
    };
    handlePOSTResponse = handlePOSTResponse.bind(this);

    fetch('/api/numberplates/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        'owner': this.state.new_owner_id,
        'number': this.state.new_number_plate
      })
    }).then(handlePOSTResponse).catch(function (err) {
    });
  };

  render() {
    return ([
      <tr>
        <td colspan="3">
          <form onSubmit={ this.handleCreate }>
            <ErrorMessage error_message={ this.state.error_message }/>
              <input type="text" placeholder="Number plate" size="12" onChange={ this.handleNumberPlateChange } value={ this.state.new_number_plate } />
              <select value={ this.state.new_owner_id } onChange={this.handleOwnerChange}>
                <OwnerOptions owners={ this.props.owners } show_no_selection={ true } />
              </select>
              <button type="submit"> Create </button>
          </form>
        </td>
      </tr>,
      this.props.number_plates.map(data => {
        return <NumberPlate number={data.number} number_plate_id={data.id} owner={data.owner} owner_full_name={data.owner_full_name}
            onNumberPlateChange={this.props.onNumberPlateChange} onNumberPlateDelete={this.props.onNumberPlateDelete} 
            owners={ this.props.owners } />
      })
    ]);
  }
};

export default NumberPlateTable;
