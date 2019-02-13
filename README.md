# Voice Assistant API
Please do not try to setup this API without referencing the [Voice-Assistant-Boilerplate](https://github.com/connlaoi/voice-assistant-boilerplate) first to see if it meets your needs.

---
### Registration Requirements

It is important to note this API requires a number of services to be registered and configured for before use.
- GitHub
    - Make sure you have cloned this into a project that you can access, it's important!
- Snips
- Google API (OPTIONAL) 
    - Needed for WaveNet TTS. Google also requires a credit card for access to advanced APIs.)
- Heroku

---

## Step 1
### Snips Setup
Before using the API you will require a Snips account and project with some basic intents created.

You can use the guide below as reference to get started.

#### Login/Create a [snips.ai](https://snips.ai) Account
> Simple enough...

![Snips - Login](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_create_account.jpg "Create an Account or Login")

#### Select/Create an Assistant
> EZ...
>
> You can ignore the hotword option on the next page.
>
> It is only necessary when using snips standalone.
>
> We will be using artyom to detect our hotword instead.

![Snips - Create Assistant](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_create_assistant.jpg "Create an Assistant or Use an existing one")

#### Name your Assistant & Select your Language
> Jarvis, what's a cool nickname?

![Snips - Name Assistant](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_name_assistant.jpg "Name Assistant & Select Language")

#### Select Add New App, then Create New App

![Snips - Create App](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_create_app.jpg "Create New App")

#### Name your App

![Snips - Name App](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_create_app_d.jpg "Name App")

#### Create New Intent

![Snips - Create Intent](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_create_intent.jpg "Create Intent")

#### Edit your Intent

![Snips - Edit Intent](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_edit_intent.jpg "Edit Intent")

#### Deploy your App

![Snips - Deploy Assistant](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_deploy_assistant.jpg "Deploy Assistant")

#### Extract NLU Engine

![Snips - Extract nlu_engine](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_extract_nlu.jpg "Extract nlu_engine")

> Move/Copy the 'nlu_engine' folder into the root directory of the API

![Snips - Extract nlu_engine root](https://github.com/connlaoi/voice-assistant-api/blob/master/img/snips/snips_extract_nlu_root.jpg "Extract nlu_engine root")

#### Snips Setup Complete! :D

---

## Step 2 (OPTIONAL)
### Google API Setup
This step is only necessary if you would like to implement wavenet tts. 

You will need to setup a new project and authorize that projects API access.

This process will yield your app specific credentials in a json format.

Replace the text in the 'auth.json' file with the json generated for you by Google.

You can use the guide below as reference to get started.

#### Login/Create a [Google Cloud Platform](https://console.cloud.google.com) Account

#### Create a New Project
> Next to the Google Cloud Platform text in the top left nav-bar, click the dropdown and select 'New Project' from the modal that follows.
>
> Enter your details and after submitting wait for the notification to say complete.
>
> Once it does, click the notification to open your new project.

![Google - New Project](https://github.com/connlaoi/voice-assistant-api/blob/master/img/google/new_project.png "New Project")

#### Navigate
> Select 'APIs & Services' from the left slider menu and navigate to the dashboard.

#### Enable APIs & Services
> On the top of this page, select the 'Enable APIs & Services' button to open the search page.
>
> Enter 'speech' and look for 'Cloud Text to Speech API'. Select it to continue.
>
> On the next page, simply select the 'Enable' button.
>
>> If you do not currently have payment authorized on your account you will be prompted here.

![Google - Enable APIs & Services](https://github.com/connlaoi/voice-assistant-api/blob/master/img/google/api_cloud_tts.png "Enable APIs & Services")

#### Credentials

> After enabling successfully, select 'Credentials' from the left slider menu to continue.
>
> On the next page, select the 'Cloud Text to Speech API' from the dropdown and then click the 'What credentials do I need?' button.

![Google - Credentials](https://github.com/connlaoi/voice-assistant-api/blob/master/img/google/api_credentials.png "Credentials")

> Next, fill out the form like below (but with your own details), making sure to select JSON.
>
> Click continue, and select 'Create without Role' (unless you want one).

![Google - Credentials Add](https://github.com/connlaoi/voice-assistant-api/blob/master/img/google/api_credentials_add.png "Credentials Add")

> A JSON file should download momentarily

![Google - Credentials Copy](https://github.com/connlaoi/voice-assistant-api/blob/master/img/google/api_credentials_copy.png "Credentials Copy")

>> Copy the contents into the 'auth.json' file in the root directory.

![Google - Credentials Location](https://github.com/connlaoi/voice-assistant-api/blob/master/img/google/api_credentials_added.png "Credentials Location")

#### Google Cloud Platform Setup Complete! :D

---

## Step 3
### Heroku Setup
This should run pretty easily on Heroku if you follow the steps below:

#### Login/Create a [Heroku](https://id.heroku.com/login) Account

> Once logged in, you will need to create a new Heroku application.

#### Create a New Project
> On the right side of your screen click the 'New' button and select 'Create new app'.
>
> Enter the details of your choosing and click 'Create app' to continue.
>
> On the next page, select GitHub under 'Deployment Method'.

![Heroku - New App](https://github.com/connlaoi/voice-assistant-api/blob/master/img/heroku/create_new_app.png "New App")

#### Connect to GitHub Repo
> If you have not linked your GitHub account with Heroku yet, now is the time do so.
>
> Once you have, search for the name of THIS cloned repository on your GitHub account.
>> Click 'Connect' when you find it to continue.

![Heroku - Search](https://github.com/connlaoi/voice-assistant-api/blob/master/img/heroku/search_github.png "Search")

#### Enable Automatic (EZ) Deployment
### IMPORTANT: Read carefully!
Next, we need to enable automatic deployments.

This ensures any new push to 'master' will update our build on Heroku automatically.

Heroku will install the python modules in our 'requirements.txt' file when loading our app.
>
> !! AFTER pushing to Heroku for the first time we need to modify our 'requirements.txt' and uncomment the remaining modules.
>
> !! COMMIT those changes and push to your repo again, but ONLY after it has successfully built the first time which you can check under 'Activity'.
>
>> This is to resolve a dependency issue.
>> If you know a better way for us to avoid this issue.
>>
>> Please let us know [here](https://github.com/connlaoi/voice-assistant-api/issues/new "GitHub New Issue")!
>
>##### Initial deploys will need to click the 'Deploy Branch' button under 'Manual Deploy'
>
>##### Or simply make changes and push to the repository again

#### Heroku Setup Complete! :D

---

## Step 4
### Putting it All Together
At this point, you should be registered for Snips, Google*, Heroku, and hopefully GitHub.

Please make sure you have both the 'voice-assistant-boilerplate' and 'voice-assistant-api' repositories installed before continuing.

Now that our API is in place. We can use our new API requests to serve to our website!

---

#### Congratulations, you now have an API for serving a voice assistant!

#### Continue by completing the [Voice Assistant Boilerplate Prerequisites](https://github.com/connlaoi/voice-assistant-boilerplate#prerequisites)

---

## Authors

* **Connlaoi Smith** - *Ongoing Development* - [connlaoi](https://github.com/connlaoi)

## Acknowledgments

* **Steve Bakos** - *Initial work on snips, artyom, & python api* - [steve-bakos](https://github.com/steve-bakos)
* **Neil Gaspar** - *Initial work on snips, artyom, & python api* - [neil-gaspar](https://github.com/neilgaspar)

See also the list of [contributors](https://github.com/connlaoi/voice-assistant-api/graphs/contributors) who participated in this project.
