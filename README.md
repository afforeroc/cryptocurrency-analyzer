# Cryptocurrency analyzer from Tidex API
This program analyze Ethereum (eth_btc) and Litecoin (ltc_btc) values from Tidex API, using a csv file as database and matplotlib to vizualize cryptocurrencies behavior in real time.
Additional, it contains a tutorial of configuration and use.

## Tutorial
This tutorial was designed to be done on a personal computer and their steps require using command-line interpreter, text editor, etc.

### Required software
* Command-line interpreter like Terminal, PowerShell, etc.
* Text editor like Notepad++, Visual Studio Code, etc.

### 1. Install Python and their necessary libraries
1.1 Install stable/latest version of [Python 3](https://www.python.org/downloads/).

1.2 Verify Python installation.
> Command-line
```
py -3 --version
```
```
pip3 --version
```

1.3 Install and verify PLY library.
> Command-line
```
pip3 install ply
```
```
pip3 show ply
```

> If you can't see the library version on Windows, launch a PowerShell window as an administrator and enter this following command. Later, try again to verify.
> Command-line
```
Set-ExecutionPolicy Unrestricted
```

### 2. Run the apps
2.1 Run the apps locally in this way.<br>
* Run the first program. It save data of the eth_btc and ltc_bth sell and buy data in csv file.
> Command-line
```
python gen_data.py
```

* And without closing the first program, open another command-line interpreter and run the second program. It graph the behavior of the eth_btc and ltc_bth sell and buy data.
> Command-line
```
python plot_rt.py
```

2.2 See results of executions of app.<br>
* Results from `gen_data.py`
> Command-line e.g.
```
high            low             avg             vol             vol_cur         last            buy             sell            updated
2.2249600E-02   2.1767100E-02   2.2008350E-02   3.1415727E+01   1.4272499E+03   2.2106300E-02   2.2056480E-02   2.2174120E-02   1589864150      
2.2249600E-02   2.1767100E-02   2.2008350E-02   3.1415727E+01   1.4272499E+03   2.2106300E-02   2.2056560E-02   2.2174120E-02   1589864151      
2.2249600E-02   2.1767100E-02   2.2008350E-02   3.1415727E+01   1.4272499E+03   2.2117100E-02   2.2056570E-02   2.2174120E-02   1589864152      
2.2249600E-02   2.1767100E-02   2.2008350E-02   3.1425571E+01   1.4276949E+03   2.2117100E-02   2.2056600E-02   2.2174120E-02   1589864153      
2.2249600E-02   2.1767100E-02   2.2008350E-02   3.1435646E+01   1.4281505E+03   2.2117500E-02   2.2056700E-02   2.2174120E-02   1589864154      
2.2249600E-02   2.1767100E-02   2.2008350E-02   3.1435646E+01   1.4281505E+03   2.2117500E-02   2.2056710E-02   2.2174120E-02   1589864155 
```

* Results from `plot_rt.py`
> Command-line e.g.
```
hour             sell            buy
00:02:23         0.02207177      0.02217492
00:02:23         0.02207177      0.02217492
00:02:25         0.02207177      0.02217492
00:02:25         0.02207177      0.02217492
00:02:26         0.02207187      0.02217492
00:02:27         0.02207188      0.02217492
```

2.3 Stop the apps.<br>
Close the second app closing the matplotlib window and after, use <kbd>ctrl</kbd> + <kbd>C</kbd> key combination to close the first program.