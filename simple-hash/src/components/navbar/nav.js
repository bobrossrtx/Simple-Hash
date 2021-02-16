import './nav.css'

function navbar() {
    return (
        <div className="navbar">
            <h1 className="nav-title">
                    Simple <span>Hash</span>
            </h1>
            <div className="nav-util">
                <ul className="nav_list">
                    <li>
                        <a className="nav-button" href="/">
                            Home
                        </a>
                    </li>
                    <li>
                        <a className="nav-button" href="/download">
                            Download
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    );
}

export default navbar;