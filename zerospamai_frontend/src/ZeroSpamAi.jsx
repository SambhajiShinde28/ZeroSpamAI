import React, { useRef, useState } from "react";
import "./ZeroSpamAiDesign.css"
import axios from "axios";


const ZeroSpamAi = () => {

    const emailFieldRef = useRef()

    const [spamPercentage,setSpamPercentage] = useState("None")
    const [notSpamPercentage,setNotSpamPercentage] = useState("None")
    const [category,setCategory] = useState("Null")

    const AnalyseBTNClicked=async()=>{
        
        if (emailFieldRef.current.value !== "") {

            const response = await axios.post("http://127.0.0.1:8000/spam", {email:emailFieldRef.current.value});
        
            if (response.data.Message === "prediction") {
                
                setSpamPercentage(response.data.SpamPercentage)
                setNotSpamPercentage(response.data.NotSpamPercentage)

                if (response.data.Category === "NotSpam") {
                    setCategory("✅ Good News! This Email is Safe.<br/><br/>This email doesn't appear to be spam. You can read or respond to it without worry.")
                }
                else{
                    setCategory("🚨 Alert! This Email is Classified as SPAM 🚨<br/><br/>⚠️ Be cautious! This email appears to be unwanted or potentially harmful. Avoid clicking on links or sharing personal information. Stay safe!")
                }
            }
            else {
                alert("Something is going to wrong, Please try again !!");
            }

        }
        else{
            alert("E-mail input text field is empty!")
        }
    }

    return (
        <div className="main-container">

            <div className="header">
                <h1>ZeroSpam-AI</h1>
            </div>

            <div className="continer">

                <div className="herosection">
                    <h2>Empowering Your Inbox</h2>
                    <h3>Let ZeroSpamAI Be Your Shield Against Unwanted Emails!<br></br> Stay Focused, Stay Protected !</h3>
                </div>

                <div className="form-continer">
                    <div className="fold">
                        <h1>Categorize E-mail</h1>
                        <textarea ref={emailFieldRef} className="inputTextarea" rows="10" cols="50" placeholder="Type E-mail Text Here.." />
                        <input type="submit" name="" value="Analyze" onClick={AnalyseBTNClicked} />
                    </div>
                </div>

                <div className="eamil-result">
                    <h1>Prediction Result</h1>
                    <p className="prediction" dangerouslySetInnerHTML={{ __html: category }}></p>

                    <div className="result-chart">
                       <p className="SpamPercentage">Spam Percentage : {spamPercentage}</p>
                       <p className="NotSpamPercentage">Not Spam Percentage : {notSpamPercentage}</p>
                    </div>
                </div>

            </div>

        </div>
    )
}

export default ZeroSpamAi