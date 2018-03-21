# pudb-microworkshops

1. Download the repository

    `git clone https://github.com/Anaaa/pudb-microworkshops.git`
    
2. Make a virtual environment

    `virtualenv -p python3.6 pudb-venv`
    
3. Activate the virtual environment

    `source pudb-venv/bin/activate`
    
4. Install requirements

    `pip install -r requirements.txt`
    
5. Have fun!


To deactivate the virtual environment run `deactivate`

1st task: find what is wrong and fix it. Do you know what have happened? 

    python -m proj.case_1
    
2nd task: make the script print `Start`, `Finish`, `The end`, do not change the range

    python -m proj.case_2
    
3rd task: make the script print `This is the end` instead of a generator representation like `<generator ...>`

    python -m proj.case_3
