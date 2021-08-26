# ppl_car_hacking
### install required libraries
- `pip install pandas`
- `pip install numpy`
- `pip install matplotlib`
- `pip install sklearn`
- `pip install tensorflow-gpu`
- `pip install --upgrade tensorflow-probability`

### format the normal action data set
On linux run the follow code to convert txt file format to csv file

Original format:

Timestamp: 1479121500.969313        ID: 0140    000    DLC: 8    00 00 00 00 1a 00 24 ee

Expected format:

1479121500.969313,0140,8,00,00,00,00,1a,00,24,ee


- `sed -i 's/Timestamp: //g' normal_run_data.txt`
- `sed -i 's/        ID: /,/g' normal_run_data.txt`
- `sed -i 's/    000    DLC: /,/g' normal_run_data.txt`
- `sed -i 's/    /,/g' normal_run_data.txt`