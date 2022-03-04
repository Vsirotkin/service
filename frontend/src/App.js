import React from 'react';
import './App.css';
import UserList from './components/User.js'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    const users = [
      {
        'username': 'IBunin',
        'first_name': 'Ivan',
        'last_name': 'Bunin',
        'email': 'ivan@gmail.com',
      },
    ]
    this.setState(
        {
          'users': users
        }
    )
  }

  render () {
    return (
        <div>
          <UserList users={this.state.users} />
        </div>
    )
  }

}

export default App;
