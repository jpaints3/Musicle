import React, {Component} from 'react';
import {render} from 'react-dom';
import PlaylistApp from './PlaylistApp.js';


class Main extends Component{
    render(){
        return (
            <playlist/>
        );
    }
}

const playlist = ({}) => {
    return (
        <div>
            <p>Am I working?</p>
        </div>
    );
}


render(<Main/>, document.getElementById("root"))


