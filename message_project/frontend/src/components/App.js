import React, { Component } from "react";
import { createRoot } from "react-dom/client";  // Use createRoot instead of render

export default class App extends Component {  // Fix typo: Conponent -> Component
    constructor(props) {
        super(props);
    }

    render() {
        return  <div>
                    <form method="POST">
                        <h1>Test</h1>
                        <label htmlFor="username">Naudotojo vardas</label>
                        <input type="text" id="username"></input>
                        <input type="submit" value="submit"></input>
                    </form>
                </div>;
    }
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);  // Create a root
root.render(<App />);  // Use root.render instead of render