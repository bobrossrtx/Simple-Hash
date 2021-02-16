function home() {
    return (
        <div className="home">
            <div className="top-ar">
                <div className="title">
                    Simple Hash
                </div>
                <div className="top-bt">
                    <a href="/download">
                        Download <i className="fa fa-download" aria-hidden="true"></i>
                    </a>
                </div>
            </div>
            <div className="cop">
                <for>
                <label className="cop-sl">
                    Password Checker
                </label>
                <input id="pw" type="password" className="cop-search" />
                <input type="submit" id="cop-search-sub" value="Check" className="cop-sub button btn-g" />
                </for>
                <h4 class="cop-res">Result<br/><span id="cop-res"></span></h4>
                <p className="cop-xpl">
                    <h3 className="cop-xpl-title">How To</h3>
                    All you have to do is enter the password you want to check and it will scan through the dictionary to see if your password has been leaked.
                </p>
            </div>
        </div>
    )
}

export default home