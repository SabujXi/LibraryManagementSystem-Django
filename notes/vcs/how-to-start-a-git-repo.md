# How to Start/Create a Git Repository
## Method One
`$ git init`

This will create a new git repository.

OR

`$ git init --bare`

This will create a new bare git repository. 

What is a bare repository?: Bare repositories that do not have a default working/checkout directory.

So, what is working directory?: Simply put, look at our project folder where we are writing our code. For our project this is where we are fetching file from git repository & saving changes when we are commiting.

## Method Two
We are already working in this method. Take a ssh/https git repository url (or even local system path) and run `clone` command.

Example:
```shell script
$ git clone https://github.com/SabujXi/LibraryManagementSystem-Django.git
``` 

--------
This text is copyrighted to Md. Sabuj Sarker (md.sabuj.sarker@gmail.com) - no part of it can be used/copied without explicit permission from him.
 