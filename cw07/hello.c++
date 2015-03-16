#include <Python.h>
#include <iostream>

//    PyObject * PyInit_hello(void);
extern "C" {
    void inithello(void);
}

using namespace std;

PyObject *hello(PyObject *self, PyObject *args) {
    cout << "hello" << endl;
    Py_INCREF(Py_None);
    return Py_None;
};

//PyObject *hello(PyObject *self, PyObject *args, PyObject *kwargs) {
//};


static PyMethodDef methods[] = {
    {"hello", (PyCFunction)hello, METH_VARARGS,
        "do nothing.\n"},
    {NULL, NULL, 0, NULL}
};

/*
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "hello",

    "do nothing in the most epic way possible.\n"
    "\n"
    "This is a very nice module",

    -1,
    methods
};

// This is for python 3:
PyMODINIT_Func
PyInit_hello(void) {
  return PyModule_Create(module);
}
*/

// This is for python 2
void inithello(void) {
  Py_InitModule("hello", methods);
}
