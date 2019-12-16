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
Uses any or a combination of existing works, but applied in the Tagalog language. For this project, NVIDIA's tacotron2 and waveglow provided the best result despite the networks being optimized for single-speaker data and our tagalog dataset being multi-speaker. This might be because, given that tacotron2 trains on per-character level, it properly learns the speaker-dependent features such as prosody. Hence, the network was able to capture this information but fails in modeling the voice.

Training tacotron2: python train.py --output_directory outdir --log_directory logdir -c \[optional, checkpoint file]
Training waveglow: python train.py -c config.json
Training deepvoice3: python train.py --data-root=\[data file] --preset=\[preset file] --checkpoint=\[optional, checkpoint file]

Please change necessary parameters in respective config files to match data.
