#!/bin/bash

verificar_pip() {
    echo "Checking if pip is installed..."
    if command -v pip &>/dev/null; then
        echo "pip is already installed."
    else
        echo "Installing pip..."
        python3 -m ensurepip --upgrade
        if [ $? -eq 0 ]; then
            echo "pip has been installed correctly.."
        else
            echo "Error"
            exit 1
        fi
    fi
}

instalar_cryptography() {
    echo "Installing cryptography..."
    pip install cryptography --break-system-packages
    if [ $? -eq 0 ]; then
        echo "¡Cryptography has been installed correctly.!"
    else
        echo "Error"
        exit 1
    fi
}

verificar_pip
instalar_cryptography
