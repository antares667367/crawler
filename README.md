# STASI CRAWLER

## 1.Quick description

This script is a program manager of security correctives multi-platforms (Windows, GNU/Linux, BSD & MacOsX).

## 2.Project state
#### **In progress**


**Part. 1 - Update Database (-u)**

*100% - Complete*

-----
**Part. 2 - Check Vulnerabilities (-c)**

*75% - Begin*

----
**Part. 3 - List Vulnerabilities (-l)**

*0% - Begin*

----------

## 3.Description
This script is a program manager of security correctives on all different systems (Windows, GNU/Linux, BSD & MacOsX).
He supports all file types (a.out, ELF, PE, COFF etc...)

We use a database to avoid some searches on each execution.

The project will be in three parts :

##### Update Database of local binary files

```sh
./StasiCrawler -u <--updatedatabase> [-f database_filepath]
```

On first time, the program takes a fingerprint of the running environment to know the type of binary files.
Then, he browses all files on the system and register path's file, hash's file and version's file on Tiny Database.

___Json Database seems like :___

|File       |Hash       |Version        |CVE        |
| --------- |:---------:|---------------|-----------|
|$path      |$hash      |$version       |$cve
|$path2     |$hash2     |$version2      |$cve2

##### Check vulnerabilities
```sh
./StasiCrawler -c <--checkvuln> [-f binary_filepath]
```
Browse all path's binary file on database, identify versions and check vulnerabilities nearby CVE (Common Vulnerabilities and Exposures).

##### Display vulnerabilities
```sh
./StasiCrawler -l <--listvuln> [-f binary_filepath]
```
Give history of all binary files vulnerable found with CVE

## 4.Set up, quick configuration
### Create virtual environment
To use our **Statsi Crawler**, you have to create a virtual environment with Virtualenv.
```sh
cd /home/username
mkdir venv
cd /home/username/venv
python3 -m venv eboutique --without-pip
source eboutique/bin/activate
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
deactivate
source eboutique/bin/activate
pip --version
```

## 5.Licences
Open Source
## 6.Documentation
### API used
#### 1.TinyDB
>TinyDB is a lightweight document oriented database optimized for your happiness :)
>It's written in pure Python and has no external dependencies.
>The target are small apps that would be blown away by a SQL-DB or an external database server.

[Git Documentation](https://github.com/msiemens/tinydb)

#### 2. Ricco API
>This API recovers in local the actual CVE online.

[No doc]()

### Modules used
##### 1.Platform
>The platform module in Python is used to access the underlying platform’s data,
>such as, hardware, operating system, and interpreter version information.
>The platform module includes tools to see the platform’s hardware, operating
>system, and interpreter version information where the program is running.

[Platform Documentation](https://docs.platform.sh/)

##### 2.Magic
>python-magic is a python interface to the libmagic file type identification library.
>libmagic identifies file types by checking their headers according to a predefined list of file types.
>This functionality is exposed to the command line by the Unix command file.

[Git documentation](https://github.com/ahupp/python-magic)

##### 3.GetOpt
>This module helps scripts to parse the command line arguments in sys.argv.
>It supports the same conventions as the Unix getopt() function (including the special meanings of arguments of the form '-' and '--').
>Long options similar to those supported by GNU software may be used as well via an optional third argument.

[Git documentation](https://github.com/python/cpython/blob/master/Lib/getopt.py)

##### 4.Fnmatch
>The fnmatch module is used to compare filenames against glob-style patterns such as used by Unix shells.

[Pymotw documentation](https://pymotw.com/2/fnmatch/)

##### 5.Beautiful Soup
>Beautiful Soup is a Python library for pulling data out of HTML and XML files.
>It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
>It commonly saves programmers hours or days of work.

[Documentation](http://beautiful-soup-4.readthedocs.io/en/latest/)

## 7. Authors

__ESD 13__ - Aston Project

@antares667367

@tonyESD

@bnoncleben

## 8.Contributing
Whether reporting bugs, discussing improvements and new ideas or writing extensions.
## 9.Changelog
#### v1.0.0 (2018-02-16)

* First official release - Deadline Project
