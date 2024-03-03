# Whisper-large-v3 with Faster-Whisper
Whisper-large-v3 is a pre-trained model for automatic speech recognition (ASR) and speech translation. It is part of the Whisper series developed by OpenAI.

## Deploy Whisper-large-v3 using Inferless:
- Deployment of Whisper-large-v3 model using [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper).
- By using the Faster-Whisper, you can expect an average latency of 0.55 sec.

---
## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the app.py according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

---
## Quick Start
Here is a quick start to help you get up and running with this template on Inferless.

### Download the inferless-runtime-config and Create a runtime 
Get started by downloading the inferless-runtime-config.yaml file and go to Inferless dashboard and create a custom runtime 

Quickly add this as a Custom runtime

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Add Your Hugging Face Auth Token
Go into the `app.py` and replace `<your_token>` with your hugging face api key. This token will be used to download weights from hugging face if you're using Llama-2. Make sure to check the repo is private to protect your hugging face key.


### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

Select the PyTorch as framework and choose **Repo(custom code)** as your model source and use the forked repo URL as the **Model URL**.

After the create model step, while setting the configuration for the model make sure to select the appropriate runtime.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/github-custom-code) for more information on model import.

The following is a sample Input and Output JSON for this model which you can use while importing this model on Inferless.

### Input
```json
{
  "inputs": [
    {
      "data": [
        "http://thepodcastexchange.ca/s/Porsche-Macan-July-5-2018-1.mp3"
      ],
      "name": "audio_url",
      "shape": [
        1
      ],
      "datatype": "BYTES"
    }
  ]
}
```

### Output
```json
{
  "outputs": [
    {
      "data": [
        "data"
      ],
      "name": "transcribed_output",
      "shape": [
        1
      ],
      "datatype": "BYTES"
    }
  ]
}
```

---
## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.
```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
                "inputs": [
                    {
                    "data": [
                        "http://thepodcastexchange.ca/s/Porsche-Macan-July-5-2018-1.mp3"
                    ],
                    "name": "audio_url",
                    "shape": [
                        1
                    ],
                    "datatype": "BYTES"
                    }
                ]
                }
            '
```


---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.pipe = None`.


For more information refer to the [Inferless docs](https://docs.inferless.com/).
