import React, { Component } from 'react';
import OwnerOptions from './OwnerOptions';
import ErrorMessage from './ErrorMessage';


class NumberPlate extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
        error_message: null,
        editable: false
      };
      this.onNumberPlateChange = this.onNumberPlateChange.bind(this);
      this.onOwnerChange = this.onOwnerChange.bind(this);
      this.onDelete = this.onDelete.bind(this);
      this.toggleEditable = this.toggleEditable.bind(this);
    };

    onNumberPlateChange(event) {
        this.props.onNumberPlateChange({
          id: this.props.number_plate_id,
          number: event.target.value,
          owner: this.props.owner,
          owner_full_name: this.props.owner_full_name
        })
    };

    onOwnerChange(event) {
      var owner_full_name = '';
      for (var i=0; i < this.props.owners.length; i++) {
        if (this.props.owners[i].id.toString() === event.target.value.toString()) {
          owner_full_name = this.props.owners[i].first_name + ' ' + this.props.owners[i].last_name;
          break;
        };
      };

      this.props.onNumberPlateChange({
        id: this.props.number_plate_id,
        number: this.props.number,
        owner:  event.target.value,
        owner_full_name: owner_full_name
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

        fetch('/api/numberplates/'+ this.props.number_plate_id + '/' , {
          method: 'PATCH',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            'owner': this.props.owner_id,
            'number': this.props.number_plate,
            'id': this.props.number_plate_id})
        }).then(handlePATCHresponse);
      } else {
        this.setState({editable: true});
      };
    };

    onDelete() {
      this.props.onNumberPlateDelete(this.props.number_plate_id);
    };

    render() {
      if (this.state.editable === true) {
        return (
        <tr>
          <td>
            <ErrorMessage error_message={ this.state.error_message }/>
            <input size="7" onChange={ this.onNumberPlateChange } value={ this.props.number }/>
          </td>
          <td>
            <select id='owner-edit' ref='owner' name='owner' value={ this.props.owner } onChange={ this.onOwnerChange }>
              <OwnerOptions owners={ this.props.owners } show_no_selection={ false } />
            </select>
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
          { this.props.number }
        </td>
        <td>
          { this.props.owner_full_name }
        </td>
        <td>
          <button type="button" onClick={ this.toggleEditable }> Edit </button>&nbsp;
          <button type="button" onClick={ this.onDelete }> Delete </button>
        </td>
      </tr>
      );
    }
 };


export default NumberPlate;
