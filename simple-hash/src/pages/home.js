import React, { useState } from 'react';

export default function Home() {

    const [pass, setPass] = useState("");

    const handleValue = () => {
        fetch(".    /assets/Simple-Hash/pass_lists/passwords.json")
            .then(response => {response.json(); console.log(response.text())})
            .then(respJson => {
                let searchPass = pass.split(" ");

                let passwords = (
                    respJson.filter((string) => {
                        let containsAtLeastOneWord = false;
                        searchPass.forEach((word) => {
                            if (string.value === "") {
                                containsAtLeastOneWord = false
                            } else if (string.includes(word))
                                containsAtLeastOneWord = true
                        });
                        if (containsAtLeastOneWord) return string
                    })
                );

                if (passwords.length > 6) {
                    document.getElementById("cop-res").innerHTML = passwords
                } else {
                    document.getElementById("cop-res").innerHTML = passwords.length
                }
            }).error(err => {
                console.log(err)
            });
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
            <div className="cop">
                <for>
                <label className="cop-sl">
                    Password Checker
                </label>
                <input id="pw" onChange={(e => {
                    setPass(e.target.value);
                })} type="text" className="cop-search" />
                <input type="submit" onClick={handleValue} id="cop-search-sub" value="Check" className="cop-sub button btn-g" />
                </for>
                <h4 class="cop-res"><span class="cop-res-l">Results</span><br/><span id="cop-res"></span></h4>
                <p className="cop-xpl">
                    <h3 className="cop-xpl-title">How To</h3>
                    <p class="cop-xpl-desc">All you have to do is enter the password you want to check and it will scan through the dictionary to see if your password has been leaked in our list.</p>
                </p>
            </div>
        </div>
    )
}

// export default home