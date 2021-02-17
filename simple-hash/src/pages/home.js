/* eslint-disable react/jsx-no-target-blank */
/* eslint-disable array-callback-return */
import React, { useState } from 'react';

export default function Home() {

    const [pass, setPass] = useState("");

    const handleValue = () => {
        fetch("/pass_lists/passwords.json")
            .then(response => response.json())
            .then(respJson => {
                let searchPass = pass.split(" ");
                
                let passwords = (
                    respJson.passwords.filter((string) => {
                        let containsAtLeastOneWord = false;
                        searchPass.forEach((word) => {
                            if (string.value === "") {
                                containsAtLeastOneWord = false
                            } else if (string.includes(word))
                                containsAtLeastOneWord = true
                        });
                        if (containsAtLeastOneWord) {
                            return string
                        }
                    })
                );

                if (passwords.length <= 5) {
                    document.getElementById("cop-res").innerHTML = passwords
                } else {
                    document.getElementById("cop-res").innerHTML = passwords.length
                }
            })
    };
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
            <div className="m-desc">
                <h3 className="m-desc-title">Simple Hash</h3>
                <p className="m-desc-txt">Simple hash is a simple tool to crack passwords using one way that most people should know of, a dictionary attack!<br/>When using the tool, it grants a quick and easy way to call a dictionary attack on any hash within: <br/><span id="code-json-txt">['MD5', 'SHA1', 'SHA224', 'SHA384', 'SHA256', 'SHA512']</span><br></br>Not only can you crack passwords, you can also encrypt passwords using the exact same hash types.</p>
                <a href="https://github.com/bobrossrtx/Simple-Hash/" className="desc-btn button btn-g" target="_blank" >View Code</a>
            </div>
            <div className="cop">
                <for>
                <label className="cop-sl">
                    Password Checker <span id="case">(Case Sensitive)</span>
                </label>
                <input id="pw" onChange={(e => {
                    setPass(e.target.value);
                })} type="text" className="cop-search" />
                <input type="submit" onClick={handleValue} id="cop-search-sub" value="Check" className="cop-sub button btn-g" />
                </for>
                <h4 className="cop-res"><span className="cop-res-l">Results</span><br/><span id="cop-res"></span></h4>
                <p className="cop-xpl">
                    <h3 className="cop-xpl-title">How To</h3>
                    <p className="cop-xpl-desc">All you have to do is enter the password you want to check and it will scan through the dictionary to see if your password has been leaked in our list.</p>
                </p>
            </div>
            <div class="Warning">
                <h1>Warning:<br/>I have not made this tool to be intended for illegal use. Any illegal use of this tool is therefor responsible for their own actions. I do not take responsibility for their uses of the tool</h1>
            </div>
        </div>
    )
}

// export default home