import React, {Component} from 'react';
import {render} from 'react-dom';
import PlaylistApp from './PlaylistApp.js';


class Main extends Component{
    render(){
        return (
            <div>
                <PlaylistApp/>
            </div>
        );
    }
}


render(<Main/>, document.getElementById("root"))


