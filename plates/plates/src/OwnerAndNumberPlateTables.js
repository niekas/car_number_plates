import React, { Component } from 'react';
import NumberPlateTable from './NumberPlateTable';
import OwnerTable from './OwnerTable';


class OwnerAndNumberPlateTables extends Component {
  constructor(props) {
    super(props);
    this.state =  window.initialData;
    this.onOwnerCreate = this.onOwnerCreate.bind(this);
    this.onNumberPlateCreate = this.onNumberPlateCreate.bind(this);
    this.onNumberPlateChange = this.onNumberPlateChange.bind(this);
    this.onNumberPlateDelete = this.onNumberPlateDelete.bind(this);
    this.onOwnerChange = this.onOwnerChange.bind(this);
    this.onOwnerDelete = this.onOwnerDelete.bind(this);
  };

  onOwnerCreate(new_owner) {
    this.setState({owners: [...this.state.owners, {
      'id': new_owner.owner_id,
      'first_name': new_owner.first_name,
      'last_name': new_owner.last_name,
    }]});
  };

  onOwnerChange(owner_changed) {
    var owners = this.state.owners.map(owner => {
      if (owner.id === owner_changed.id) {
        owner.first_name = owner_changed.first_name;
        owner.last_name = owner_changed.last_name;
      };
      return owner;
    });
    this.setState({owners: owners});
  };

  onOwnerDelete(owner_id) {
    const filteredOwners = this.state.owners.filter(owner => {
      return owner.id !== owner_id;
    });
    const filteredNumberPlates = this.state.number_plates.filter(number_plate => {
      return number_plate.owner_id != owner_id;
    });
    this.setState({owners: filteredOwners, number_plates: filteredNumberPlates});

    fetch('/api/owners/' + owner_id + '/', {
      method: 'DELETE',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    });
  };

  onNumberPlateCreate(new_number_plate) {
    this.setState({number_plates: [...this.state.number_plates, {
      'id': new_number_plate.id,
      'number': new_number_plate.number,
      'owner_id': new_number_plate.owner_id,
      'owner_full_name': new_number_plate.owner_full_name,
    }]});
  };

  onNumberPlateChange(number_plate_changed) {
    var number_plates = this.state.number_plates.map(number_plate => {
      if (number_plate.id === number_plate_changed.id) {
        number_plate.number = number_plate_changed.number;
        number_plate.owner_id = number_plate_changed.owner_id;
        number_plate.owner_full_name = number_plate_changed.owner_full_name;
      };
      return number_plate;
    });
    this.setState({number_plates: number_plates});
  };

  onNumberPlateDelete(number_plate_id) {
    const filteredNumberPlates = this.state.number_plates.filter(number_plate => {
      return number_plate.id !== number_plate_id;
    });
    this.setState({number_plates: filteredNumberPlates})

    fetch('/api/numberplates/' + number_plate_id + '/', {
      method: 'DELETE',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    });
  };

  render() {
    return ([
      <div>
        <table>
          <thead>
            <tr>
              <th>Owner</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <OwnerTable owners={ this.state.owners } onOwnerCreate={ this.onOwnerCreate }
                onOwnerChange={ this.onOwnerChange } onOwnerDelete={ this.onOwnerDelete } />
          </tbody>
        </table>
      </div>,
      <div>
        <table>
          <thead>
            <tr>
              <th>Car number plate</th>
              <th>Owner</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <NumberPlateTable owners={ this.state.owners } number_plates={ this.state.number_plates }
                onNumberPlateCreate={ this.onNumberPlateCreate } onNumberPlateChange={ this.onNumberPlateChange }
                onNumberPlateDelete={ this.onNumberPlateDelete } />
          </tbody>
        </table>
      </div>
    ])
  };
};

export default OwnerAndNumberPlateTables;
