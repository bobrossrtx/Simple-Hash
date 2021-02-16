import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import Navbar from './components/navbar/nav';
import Home from './pages/home'

import './components/app.css'
import './components/button.css'

function App() {
  return (
    <div className="wrapper">
      <Navbar />
      <Router>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/download">
            {/* <Download /> */}
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
