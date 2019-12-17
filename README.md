# tts_models
A compilation of Text-to-Speech Synthesis projects

## Famous Works
### Single-Speaker TTS
1. NVIDIA's Tacotron 2<br>
    [Paper] https://arxiv.org/pdf/1712.05884.pdf<br>
    [Code] https://github.com/NVIDIA/tacotron2<br>

2. NVIDIA's OpenSeq2Seq <br>
    [Paper] https://nvidia.github.io/OpenSeq2Seq/<br>
    [Code] https://github.com/NVIDIA/OpenSeq2Seq<br>

3. Deep Convolutional TTS <br>
    [Paper] https://arxiv.org/pdf/1710.08969.pdf<br>
    [Code] https://github.com/Kyubyong/dc_tts<br>
*Implemented by a third-party and not by the writers themselves<br>
4. Google's Tacotron <br>
    [Paper] https://arxiv.org/pdf/1703.10135.pdf<br>
    [Code] https://github.com/keithito/tacotron<br>
    [Code] https://github.com/MycroftAI/mimic2<br>
*Tensorflow implementation of Tacotron, not by the writers themselves<br>
5. Mozilla Text-to-Speech<br>
    [Code] https://github.com/mozilla/TTS<br>
6. Stanford's GloVe<br>
    [Documentation] https://nlp.stanford.edu/projects/glove/<br>
    [Code] https://github.com/stanfordnlp/GloVe<br>
    
7. DeepMind's GAN-TTS
    [Documentation] https://arxiv.org/pdf/1909.11646.pdf<br>
    [Code] https://github.com/yanggeng1995/GAN-TTS<br>
### Other Directories
1. https://github.com/topics/text-to-speech<br>
2. https://github.com/topics/google-text-to-speech<br>
### Multi-Speaker TTS
1. Multi-Speaker Tacotron in TensorFlow<br>
    [Code] https://github.com/carpedm20/multi-speaker-tacotron-tensorflow<br>
2. DeepVoice Series<br>
    [DeepVoice 2] https://github.com/jdbermeol/deep_voice_2<br>
    [DeepVoice 3] https://github.com/r9y9/deepvoice3_pytorch<br>
** Most MS-TTS are unofficial code implementations

# Tagalog Text-to-Speech Synthesis
Uses any or a combination of existing works, but applied in the Tagalog language. For this project, using NVIDIA's [tacotron2](https://github.com/NVIDIA/tacotron2) and [waveglow](https://github.com/NVIDIA/waveglow) provided the best results despite the networks being optimized for single-speaker data and our tagalog dataset being multi-speaker. This might be because, given that tacotron2 trains on per-character level, it properly learns the voice-independent features such as prosody. Hence, the network was able to capture this information but fails in modeling the voice.

Training was done similar to NVIDIA and Ryuichi Yamamoto's deepvoice3. Data was edited and organised to match the expected inputs of the networks, and config files were changed to match the tagalog dataset.

Training tacotron2: `python train.py --output_directory \[output dir] --log_directory \[log dir] -c \[optional, checkpoint file]`<br>
Training waveglow (in waveglow folder): `python train.py -c config.json`<br>
Training deepvoice3 (in deepvoice3 folder): `python train.py --data-root=\[data file] --preset=\[preset file] --checkpoint=\[optional, checkpoint file]`<br>

Checkpoints can be found here: [checkpoints](https://drive.google.com/drive/folders/1CuV7v9up5PcHuPzFsOsvx9_KQ2q2O-ky?usp=sharing)<br>

#### Voice Conversion Option
Adding in Kobayashi's Sprocket was supposedly a test if whether implementing a voice conversion <i>after</i> the network would mitigate the grittiness of the output. As expected, results showed no improvements to poor performance, especially when tested with longer sentences.

Training was done by, first, generating the source voice using network and the target taken from the data. Both source and target must speak the same words. Moreover, all target data must come from a single speaker. This can be done manually. Or you can download some of our used data [here](https://drive.google.com/drive/folders/1CuV7v9up5PcHuPzFsOsvx9_KQ2q2O-ky?usp=sharing), and paste it inside `/sprocket/example/data/`

For training and/ generation, please follow the steps [here](https://github.com/k2kobayashi/sprocket/blob/master/docs/vc_example.md)
