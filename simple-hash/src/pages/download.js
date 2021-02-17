export default function Download() {
    return(
        <div className="download">
            <h1 className="d-load-title">Download Simple Hash</h1>
            <div className="download-area">
                <div className="rar">
                <div className="diag-divider" id="div1" />
                    <h2 className="download-title1">.rar</h2>
                    <p className="download-desc" id="d-desc1">For windows users:
                    extract the contents of the rar file into any directory.<br/>
                    All you then have to do is run the python script within Simple-Hash directory.
                    </p>
                    <a href="/download/Simple-Hash.rar" className="download-btn" id="d-btn1">
                        Download <i class="fa fa-download" aria-hidden="true"></i>
                    </a>
                </div>
                <div className="divider" />
                <div className="tar">
                    <h2 className="download-title2">.tar.gz</h2>
                    <div className="diag-divider" id="div2" />
                    <p className="download-desc" id="d-desc2">For linux users:
                    Extract the contents of the tar.gz file into a directory<br/>( e.g. /bin ~~~ /home/(user) )<br/>
                    run the python script within the directory
                    </p>
                    <a href="/download/Simple-Hash.tar.gz" className="download-btn" id="d-btn2">
                        Download <i class="fa fa-download" aria-hidden="true"></i>
                    </a>
                </div>
            </div>
        </div>
    )
}