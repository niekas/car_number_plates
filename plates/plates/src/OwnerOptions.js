import React, { Component } from 'react';


class OwnerOptions extends React.Component {
  render() {
    if (this.props.show_no_selection === true) {
      return ([
        <option value="-1">------------</option>,
        this.props.owners.map(function(owner) {
          return <option value={ owner.id }>{ owner.first_name } { owner.last_name }</option>
        })
      ])
    };
    return (this.props.owners.map(function(owner) {
      return <option value={ owner.id }>{ owner.first_name } { owner.last_name }</option>
    }))
  };
};

export default OwnerOptions;
