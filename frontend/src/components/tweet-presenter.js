import React from 'react';
import {ListItem} from 'material-ui/List';
import {grey400, darkBlack, lightBlack} from 'material-ui/styles/colors';

class TweetPresenter extends React.Component {
  render() {
    return (
      <div>
        <ListItem
          primaryText={
            <p>
              <span style={{color: lightBlack}}>@{this.props.tweet.user}: </span>
              <span style={{color: darkBlack}}>{this.props.tweet.text}</span>
            </p>
          }
          secondaryText={this.props.tweet.time}
          onMouseEnter={() => {this.props.onHover(this.props.tweet)}}
          onMouseLeave={() => {this.props.onLeave()}}
        />
      </div>
    )
  }
}
// Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus fringilla egestas quam, vitae molestie ex pharetra et.
export default TweetPresenter;
