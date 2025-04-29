from src.main import *
from unittest.mock import patch
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Olá Mundo!!!"}

#async def test_funcaoteste():
#    with patch('random.randint', return_value=57):
#        result = await funcaoteste()
        
#    assert result () == {"teste": True, "num_aleatorio": 57}

async def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Joao", curso="Logica", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result
    
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result
    
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result