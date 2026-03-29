"""
mini-inventory SPEC test senaryolari
Ogrenci: Tunahan Caner YILDIZ (251478112)
Proje: mini-inventory
"""

import subprocess
import os
import shutil


def run_cmd(args):
    """Komutu calistirir ve stdout sonucunu dondurur."""
    result = subprocess.run(
        ["python", "solution_v0.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def setup_function():
    """Her testten once temiz bir baslangic ortami hazirlar."""
    if os.path.exists(".miniinventory"):
        shutil.rmtree(".miniinventory")


# --- init testleri ---

def test_init_creates_directory():
    """init komutu dizin ve veri dosyasi olusturmali."""
    output = run_cmd(["init"])
    assert os.path.exists(".miniinventory")
    assert os.path.exists(".miniinventory/inventory.dat")
    assert "Initialized empty mini-inventory" in output


def test_init_already_exists():
    """Iki kez init cagrilinca uygun hata mesaji donmeli."""
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Already initialized" in output


# --- add testleri ---

def test_add_single_product():
    """Tek bir urun basariyla eklenebilmeli."""
    run_cmd(["init"])
    output = run_cmd(["add", "Pencil", "50"])
    assert "Added product #1: Pencil (50)" in output


def test_add_second_product():
    """Ikinci urun eklendiginde kimlik numarasi 2 olmali."""
    run_cmd(["init"])
    run_cmd(["add", "Pencil", "50"])
    output = run_cmd(["add", "Notebook", "20"])
    assert "Added product #2: Notebook (20)" in output


def test_add_before_init():
    """init yapilmadan add cagrilinca hata vermeli."""
    output = run_cmd(["add", "Pencil", "50"])
    assert "Not initialized" in output


def test_add_invalid_quantity():
    """Gecersiz miktar verilirse hata mesaji donmeli."""
    run_cmd(["init"])
    output = run_cmd(["add", "Pencil", "-5"])
    assert "Invalid quantity" in output


def test_add_missing_arguments():
    """Eksik arguman verilirse kullanim mesaji donmeli."""
    run_cmd(["init"])
    output = run_cmd(["add", "Pencil"])
    assert "Usage: python solution_v0.py add <name> <quantity>" in output


# --- list testleri ---

def test_list_placeholder_message():
    """v0 surumunde list komutu placeholder mesaji vermeli."""
    run_cmd(["init"])
    output = run_cmd(["list"])
    assert "Command 'list' will be implemented in future weeks." in output


def test_list_before_init():
    """init olmadan list cagrilinca hata mesaji donmeli."""
    output = run_cmd(["list"])
    assert "Command 'list' will be implemented in future weeks." in output or "Not initialized" in output


# --- update testleri ---

def test_update_placeholder_message():
    """v0 surumunde update komutu placeholder mesaji vermeli."""
    run_cmd(["init"])
    output = run_cmd(["update", "1", "80"])
    assert "Command 'update' will be implemented in future weeks." in output


def test_update_without_init_placeholder():
    """update komutu v0 surumunde placeholder mesaji vermeli."""
    output = run_cmd(["update", "1", "80"])
    assert "Command 'update' will be implemented in future weeks." in output


# --- delete testleri ---

def test_delete_placeholder_message():
    """v0 surumunde delete komutu placeholder mesaji vermeli."""
    run_cmd(["init"])
    output = run_cmd(["delete", "1"])
    assert "Command 'delete' will be implemented in future weeks." in output


def test_delete_without_init_placeholder():
    """delete komutu v0 surumunde placeholder mesaji vermeli."""
    output = run_cmd(["delete", "1"])
    assert "Command 'delete' will be implemented in future weeks." in output


# --- genel hata testleri ---

def test_unknown_command():
    """Tanimsiz komut girilirse hata mesaji donmeli."""
    run_cmd(["init"])
    output = run_cmd(["fly"])
    assert "Unknown command: fly" in output


def test_missing_command():
    """Ana komut eksikse genel kullanim mesaji donmeli."""
    output = run_cmd([])
    assert "Usage: python solution_v0.py <command> [args]" in output