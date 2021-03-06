# Deep Probabilistic Learning for Car Hacking Analysis
Please cite the following paper if you use our code. 

Laha Ale, Scott A. King, and Ning Zhang, "Deep Bayesian Learning for Car Hacking Detection", *Bayesian Deep Learning Workshop, 35th Conference on Neural Information Processing Systems*


bibtex for citing the paper: 

`
@InProceedings{aleneurips2021,
  title = 	 {Deep Bayesian Learning for Car Hacking Detection,
  author = 	 {Laha Ale, Scott King, and Ning Zhang},
  booktitle = 	 {Bayesian Deep Learning Workshop, 35th Conference on Neural Information Processing Systems},
  year = 	 {2021},
  month = 	 {6--12 Dec}
}
`

### 1. Download Data
- Request data by access [Car-Hacking Dataset for the intrusion detection](https://ocslab.hksecurity.net/Datasets/CAN-intrusion-dataset)
- Download the data files and save them into `data` folder

### 2. install required libraries 
#### 1) for ENV 1
- `pip install pandas`
- `pip install numpy`
- `pip install matplotlib`
- `pip install sklearn`
- `pip install tensorflow-gpu`
- `pip install --upgrade tensorflow-probability`
- #### 2) for ENV 2
- `pip install pandas`
- `pip install numpy`
- `pip install matplotlib`
- `pip install sklearn`
- `conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia`
- `pip install pyro-ppl`
- `pip install gpytorch`

### 3. Covert Attack-free(normal) text file to CSV
One way to process  is:
On linux run the follow code to convert txt file format to csv file

Original format:

Timestamp: 1479121500.969313        ID: 0140    000    DLC: 8    00 00 00 00 1a 00 24 ee

Expected format:

1479121500.969313,0140,8,00,00,00,00,1a,00,24,ee


- `sed -i 's/Timestamp: //g' normal_run_data.txt`
- `sed -i 's/        ID: /,/g' normal_run_data.txt`
- `sed -i 's/    000    DLC: /,/g' normal_run_data.txt`
- `sed -i 's/    /,/g' normal_run_data.txt`
- `sed -i 's/ /,/g' normal_run_data.txt`

### 4. Play with notebooks
- [int_data_small.ipynb](https://github.com/ainilaha/ppl_car_hacking/blob/main/int_data_small.ipynb)
- [bayesian_net.ipynb](https://github.com/ainilaha/ppl_car_hacking/blob/main/bayesian_net.ipynb)
- [.... more](https://github.com/ainilaha/ppl_car_hacking)
