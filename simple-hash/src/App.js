import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import Navbar from './components/navbar/nav';
import Home from './pages/home';
import Download from './pages/download';

import './components/css/app.css';
import './components/css/button.css';
import './components/css/download.css'

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
            <Download />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
