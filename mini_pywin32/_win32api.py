from __future__ import absolute_import

import ctypes
from ctypes.wintypes import (
    BOOL, DWORD, HANDLE, HMODULE, LONG, LPCWSTR, LPARAM, WCHAR, WORD)

kernel32 = ctypes.windll.kernel32

_LoadLibraryEx = kernel32.LoadLibraryExW
_LoadLibraryEx.argtypes = [LPCWSTR, HANDLE, DWORD]
_LoadLibraryEx.restype = HMODULE
_FreeLibrary = kernel32.FreeLibrary

_EnumResTypeProc = ctypes.WINFUNCTYPE(BOOL, HMODULE, LONG, LPARAM)
_EnumResNameProc = ctypes.WINFUNCTYPE(BOOL, HMODULE, LONG, LONG, LPARAM)
_EnumResLanguagesProc = ctypes.WINFUNCTYPE(
    BOOL, HMODULE, WCHAR, WCHAR, WORD, LPARAM)

_EnumResourceTypes = kernel32.EnumResourceTypesW
_EnumResourceNames = kernel32.EnumResourceNamesW
_EnumResourceLanguages = kernel32.EnumResourceLanguagesW

_LoadResource = kernel32.LoadResource
_LockResource = kernel32.LockResource
_FindResourceEx = kernel32.FindResourceExW
_SizeofResource = kernel32.SizeofResource
