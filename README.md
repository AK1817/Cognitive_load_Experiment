# Cognitive Load Test Battery

This directory implements a test battery of different experiments to trigger cognitive load.

Following tests are included:
- n-back Test
- Stroop Test
- Stroop Test with Time Pressure
- Stroop Test with an Additional Task
- Reading Span Test

Following questionaires are included:
- NASA TXL Questionaire
- POMS Emotions Questionaire
- Voice recording for Emotions

## Setup

You need to run this experiment on Windows.

Install the requirements

`pip install -r requirements.txt`

Install PsychoPy version 2021.1.4 from PsychoPy's GitHub Releases: https://github.com/psychopy/psychopy/releases 
- for Windows: https://github.com/psychopy/psychopy/releases/download/2021.1.4/StandalonePsychoPy3-2021.1.4-win64.exe 

(please choose this version, there are copatibility problems with newer versions)

Open the PsychoPy Builder, click the "open file"-button to choose and open one of the .psyexp files. Start the experiment by clicking the green arrow ("run experiment").

Set the correct screen size in PsychoPy experiment setttings >> Screen >> Window Size. You can get your screen size from http://whatismyscreenresolution.net/ 



