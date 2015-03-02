#include <Python.h>
#include <stdio.h>

static PyObject *
hello(PyObject *self, PyObject *args, PyObject *kwargs) {
	printf("Hello!\n");
	Py_RETURN_NONE;
}

static PyMethodDef methods[] = {
	{"hello", hello, METH_VARARGS|METH_KEYWORDS, "Say hello!"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"b",
	NULL,
	-1,
	methods
};

PyMODINIT_FUNC
PyInit_b(void) {
	return PyModule_Create(&module);
};
