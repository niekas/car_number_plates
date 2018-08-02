import React, { Component } from 'react';


class ErrorMessage extends Component {
    render() {
      if (this.props.error_message === null) return null;
      return (
        <div>{ this.props.error_message }</div>
      )
    };
};

export default ErrorMessage;
