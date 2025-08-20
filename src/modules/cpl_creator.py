#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v3.0 - CPL Creator
Gera o protocolo integrado de CPLs devastadores como um módulo do sistema
"""

import logging
import json
import os
from typing import Dict, Any
from datetime import datetime
from services.enhanced_ai_manager import enhanced_ai_manager
from services.auto_save_manager import salvar_etapa

logger = logging.getLogger(__name__)

async def generate_cpl_module(
    session_id: str,
    sintese_master: Dict[str, Any],
    avatar_data: Dict[str, Any],
    contexto_estrategico: Dict[str, Any],
    dados_web: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Gera o módulo de CPL como parte do fluxo principal
    
    Args:
        session_id: ID da sessão
        sintese_master: Síntese completa da análise
        avatar_data: Dados do avatar gerado
        contexto_estrategico: Contexto estratégico definido
        dados_web: Dados brutos da pesquisa web
        
    Returns:
        Dict com conteúdo do módulo CPL gerado
    """
    try:
        logger.info("🎯 Gerando módulo CPL - Protocolo Integrado de Criação de CPLs Devastadores")
        
        # Preparar contexto rico para a IA
        contexto_para_ia = {
            "sintese_analise": sintese_master,
            "avatar_cliente": avatar_data,
            "contexto_estrategico": contexto_estrategico,
            "dados_pesquisa_web": {k: v for k, v in list(dados_web.items())[:5]} if dados_web else {},
            "termos_chave": contexto_estrategico.get("termos_chave", [])[:10] if contexto_estrategico else [],
            "objecoes_identificadas": contexto_estrategico.get("objecoes", [])[:5] if contexto_estrategico else [],
            "tendencias_mercado": contexto_estrategico.get("tendencias", [])[:5] if contexto_estrategico else [],
            "casos_sucesso_reais": contexto_estrategico.get("casos_sucesso", [])[:5] if contexto_estrategico else []
        }

        prompt = f"""
# MÓDULO ESPECIALIZADO: PROTOCOLO INTEGRADO DE CRIAÇÃO DE CPLs DEVASTADORES

## CONTEXTO ESTRATÉGICO FORNECIDO:
{json.dumps(contexto_para_ia, indent=2, ensure_ascii=False)}

## INSTRUÇÕES PARA GERAÇÃO:

Com base em TODO o contexto fornecido, crie um protocolo integrado e devastador para criação de sequência de 4 CPLs (Copywriting de Alta Performance) que converta de forma excepcional.

### ESTRUTURA OBRIGATÓRIA DE SAÍDA (RETORNE APENAS JSON VÁLIDO):

```json
{{
  "titulo": "Título impactante do protocolo gerado",
  "descricao": "Descrição do protocolo e seu impacto estratégico",
  "fases": {{
    "fase_1_arquitetura": {{
      "titulo": "Arquitetura do Evento Magnético",
      "descricao": "Visão geral da arquitetura",
      "estrategia": "Estratégia central da fase",
      "versoes_evento": [
        {{
          "tipo": "Agressiva/Polarizadora|Aspiracional/Inspiradora|Urgente/Escassa",
          "nome_evento": "Nome magnético do evento",
          "justificativa_psicologica": "Justificativa do nome",
          "promessa_central": "Promessa paralisante",
          "mapeamento_cpls": {{
            "cpl1": "Mapeamento psicológico CPL1",
            "cpl2": "Mapeamento psicológico CPL2",
            "cpl3": "Mapeamento psicológico CPL3",
            "cpl4": "Mapeamento psicológico CPL4"
          }}
        }}
      ],
      "recomendacao_final": "Recomendação de qual versão usar e por quê"
    }},
    "fase_2_cpl1": {{
      "titulo": "CPL1 - A Oportunidade Paralisante",
      "descricao": "Descrição da CPL1",
      "teasers": [
        {{
          "texto": "Texto do teaser baseado em frases EXATAS coletadas",
          "justificativa": "Por que esta frase é eficaz"
        }}
      ],
      "historia_transformacao": {{
        "antes": "Situação inicial do avatar (baseada em dados reais)",
        "durante": "Processo de transformação (baseado em casos de sucesso)",
        "depois": "Resultado final transformador (com dados reais)"
      }},
      "loops_abertos": [
        {{
          "descricao": "Descrição do loop aberto",
          "fechamento_no_cpl4": "Como será fechado no CPL4"
        }}
      ],
      "quebras_padrao": [
        {{
          "descricao": "Quebra de padrão específica",
          "base_tendencia": "Tendência que fundamenta"
        }}
      ],
      "provas_sociais": [
        {{
          "tipo": "Tipo de prova social",
          "dados_reais": "Dados concretos (se disponíveis)",
          "impacto_psicologico": "Impacto esperado"
        }}
      ]
    }},
    "fase_3_cpl2": {{
      "titulo": "CPL2 - A Transformação Impossível",
      "descricao": "Descrição da CPL2",
      "casos_sucesso_detalhados": [
        {{
          "caso": "Descrição do caso específico (se disponível)",
          "before_after_expandido": {{
            "antes": "Situação antes (com dados)",
            "durante": "Processo aplicado (com termos específicos do nicho)",
            "depois": "Resultados alcançados (quantificáveis)"
          }},
          "elementos_cinematograficos": [
            "Elemento 1 baseado em depoimentos reais",
            "Elemento 2 baseado em depoimentos reais"
          ],
          "resultados_quantificaveis": [
            {{
              "metrica": "Métrica medida",
              "valor_antes": "Valor inicial (se disponível)",
              "valor_depois": "Valor final (se disponível)",
              "melhoria_percentual": "Percentual de melhoria (se calculável)"
            }}
          ],
          "provas_visuais": [
            "Tipo de prova visual 1 (se mencionado)",
            "Tipo de prova visual 2 (se mencionado)"
          ]
        }}
      ],
      "metodo_revelado": {{
        "percentual_revelado": "20-30%",
        "descricao": "Descrição do que foi revelado do método",
        "elementos_principais": [
          "Elemento 1 do método (termo específico do nicho)",
          "Elemento 2 do método (termo específico do nicho)"
        ]
      }},
      "camadas_crencia": [
        {{
          "camada_numero": 1,
          "foco": "Foco da camada",
          "dados_suporte": "Dados que sustentam (se disponíveis)",
          "impacto_psicologico": "Impacto esperado"
        }}
      ]
    }},
    "fase_4_cpl3": {{
      "titulo": "CPL3 - O Caminho Revolucionário",
      "descricao": "Descrição da CPL3",
      "nome_metodo": "Nome do método baseado em termos-chave do nicho",
      "estrutura_passo_passo": [
        {{
          "passo": 1,
          "nome": "Nome específico do passo (termo do nicho)",
          "descricao": "Descrição detalhada",
          "tempo_execucao": "Tempo estimado de execução (se inferido)",
          "erros_comuns": [
            "Erro comum 1 identificado nas buscas",
            "Erro comum 2 identificado nas buscas"
          ],
          "dica_avancada": "Dica para otimizar resultados (se inferida)"
        }}
      ],
      "faq_estrategico": [
        {{
          "pergunta": "Pergunta real identificada nas objeções",
          "resposta": "Resposta convincente baseada em dados",
          "base_dados": "Dados que fundamentam a resposta (se disponível)"
        }}
      ],
      "justificativa_escassez": {{
        "limitacoes_reais": [
          "Limitação 1 identificada nas pesquisas",
          "Limitação 2 identificada nas pesquisas"
        ],
        "impacto_psicologico": "Impacto esperado da escassez"
      }}
    }},
    "fase_5_cpl4": {{
      "titulo": "CPL4 - A Decisão Inevitável",
      "descricao": "Descrição da CPL4",
      "stack_valor": {{
        "bonus_1_velocidade": {{
          "nome": "Nome do bônus",
          "descricao": "Descrição do valor entregue",
          "dados_tempo_economizado": "Dados concretos de tempo economizado (se disponível)",
          "impacto_avatar": "Impacto real no avatar"
        }},
        "bonus_2_facilidade": {{
          "nome": "Nome do bônus",
          "descricao": "Descrição do valor entregue",
          "friccoes_eliminadas": [
            "Fricção 1 eliminada (baseada em objeções)",
            "Fricção 2 eliminada (baseada em objeções)"
          ],
          "facilitadores_inclusos": [
            "Facilitador 1",
            "Facilitador 2"
          ]
        }},
        "bonus_3_seguranca": {{
          "nome": "Nome do bônus",
          "descricao": "Descrição do valor entregue",
          "preocupacoes_enderecadas": [
            "Preocupação 1 encontrada",
            "Preocupação 2 encontrada"
          ],
          "mecanismos_protecao": [
            "Mecanismo 1",
            "Mecanismo 2"
          ]
        }},
        "bonus_4_status": {{
          "nome": "Nome do bônus",
          "descricao": "Descrição do valor entregue",
          "aspiracoes_atendidas": [
            "Aspiração 1 identificada nas redes",
            "Aspiração 2 identificada nas redes"
          ],
          "elementos_exclusivos": [
            "Elemento 1",
            "Elemento 2"
          ]
        }},
        "bonus_5_surpresa": {{
          "nome": "Nome do bônus surpresa",
          "descricao": "Descrição do valor entregue",
          "elemento_inesperado": "Elemento que não foi mencionado nas pesquisas",
          "valor_percebido": "Alto/Médio/Baixo + justificativa"
        }}
      }},
      "precificacao_psicologica": {{
        "valor_base": "Valor definido com base em pesquisa de mercado (se inferido)",
        "comparativo_concorrentes": [
          {{
            "concorrente": "Nome do concorrente (se identificável)",
            "oferta": "Descrição da oferta (se identificável)",
            "preco": "Preço do concorrente (se identificável)",
            "diferencial_posicionamento": "Como se posicionar melhor"
          }}
        ],
        "justificativa_precificacao": "Justificativa baseada em dados reais de valor entregue"
      }},
      "garantias_agressivas": [
        {{
          "tipo_garantia": "Tipo de garantia oferecida",
          "descricao": "Descrição detalhada",
          "dados_suporte": "Dados reais que fundamentam a garantia (se disponíveis)",
          "periodo_cobertura": "Período de cobertura da garantia",
          "processo_resgate": "Como o cliente resgata a garantia"
        }}
      ]
    }}
  }},
  "consideracoes_finais": {{
    "impacto_previsto": "Impacto estratégico previsto da sequência CPL",
    "diferenciais": [
      "Diferencial 1 do protocolo",
      "Diferencial 2 do protocolo"
    ],
    "proximos_passos": [
      "Passo 1 para implementação",
      "Passo 2 para implementação"
    ]
  }}
}}
```

IMPORTANTE:
- Use APENAS dados reais fornecidos no contexto. Se um dado não estiver disponível, indique claramente (ex: "Não especificado nos dados").
- Foque em insights acionáveis e estratégias comprovadas.
- A saída DEVE ser um JSON válido, SEM markdown adicional além do bloco json de saída.
"""

        # Usar a IA com busca ativa para gerar o conteúdo do módulo
        conteudo_modulo = await enhanced_ai_manager.generate_with_active_search(
            prompt=prompt,
            context=json.dumps(contexto_para_ia, indent=2, ensure_ascii=False),
            session_id=session_id,
            max_search_iterations=2  # Menos iterações para módulo específico
        )

        # Tentar parsear o JSON retornado
        try:
            modulo_cpl = json.loads(conteudo_modulo)
            logger.info("✅ Módulo CPL gerado com sucesso")

            # Salvar o módulo gerado
            salvar_etapa("cpl_completo", modulo_cpl, categoria="modulos_principais", session_id=session_id)

            return modulo_cpl

        except json.JSONDecodeError:
            logger.error("❌ Erro ao parsear JSON do módulo CPL")
            # Fallback com estrutura básica
            fallback_cpl = {
                "titulo": "Protocolo de CPLs Devastadores",
                "descricao": "Protocolo gerado com base nos dados estratégicos disponíveis",
                "fases": {},
                "consideracoes_finais": {
                    "impacto_previsto": "Não aplicável",
                    "diferenciais": [],
                    "proximos_passos": ["Verificar logs de erro", "Tentar regenerar o módulo"]
                }
            }
            salvar_etapa("cpl_completo", fallback_cpl, categoria="modulos_principais", session_id=session_id)
            return fallback_cpl

    except Exception as e:
        logger.error(f"❌ Erro ao gerar módulo CPL: {str(e)}")
        # Retornar estrutura mínima em caso de erro
        erro_cpl = {
            "titulo": "Protocolo de CPLs - Erro na Geração",
            "descricao": f"Não foi possível gerar o protocolo completo devido a: {str(e)}",
            "fases": {},
            "consideracoes_finais": {
                "impacto_previsto": "Não aplicável",
                "diferenciais": [],
                "proximos_passos": ["Verificar logs de erro", "Tentar regenerar o módulo"]
            }
        }
        salvar_etapa("cpl_erro", {"erro": str(e)}, categoria="modulos_principais", session_id=session_id)
        return erro_cpl


# Função auxiliar para validar estrutura do CPL gerado
def validar_estrutura_cpl(modulo_cpl: Dict[str, Any]) -> bool:
    """
    Valida se a estrutura do módulo CPL está correta
    
    Args:
        modulo_cpl: Dicionário com o módulo CPL gerado
        
    Returns:
        bool: True se a estrutura estiver válida, False caso contrário
    """
    try:
        # Verificar campos obrigatórios principais
        campos_obrigatorios = ["titulo", "descricao", "fases", "consideracoes_finais"]
        for campo in campos_obrigatorios:
            if campo not in modulo_cpl:
                logger.warning(f"⚠️  Campo obrigatório ausente: {campo}")
                return False

        # Verificar estrutura das fases
        fases_esperadas = [
            "fase_1_arquitetura",
            "fase_2_cpl1", 
            "fase_3_cpl2",
            "fase_4_cpl3",
            "fase_5_cpl4"
        ]
        
        fases = modulo_cpl.get("fases", {})
        for fase in fases_esperadas:
            if fase not in fases:
                logger.warning(f"⚠️  Fase ausente: {fase}")
                return False

        logger.info("✅ Estrutura do módulo CPL válida")
        return True

    except Exception as e:
        logger.error(f"❌ Erro ao validar estrutura CPL: {str(e)}")
        return False


# Função auxiliar para gerar sumário executivo do CPL
def gerar_sumario_executivo(modulo_cpl: Dict[str, Any]) -> Dict[str, Any]:
    """
    Gera um sumário executivo do módulo CPL criado
    
    Args:
        modulo_cpl: Dicionário com o módulo CPL gerado
        
    Returns:
        Dict com sumário executivo
    """
    try:
        fases = modulo_cpl.get("fases", {})
        
        sumario = {
            "titulo_protocolo": modulo_cpl.get("titulo", "Não especificado"),
            "total_fases": len(fases),
            "estrategia_principal": fases.get("fase_1_arquitetura", {}).get("estrategia", "Não especificada"),
            "evento_recomendado": None,
            "total_bonus": 0,
            "garantias_oferecidas": 0,
            "nivel_complexidade": "Médio",
            "tempo_implementacao_estimado": "7-14 dias"
        }
        
        # Extrair evento recomendado
        arquitetura = fases.get("fase_1_arquitetura", {})
        if "versoes_evento" in arquitetura and arquitetura["versoes_evento"]:
            primeiro_evento = arquitetura["versoes_evento"][0]
            sumario["evento_recomendado"] = primeiro_evento.get("nome_evento", "Não especificado")
        
        # Contar bônus
        cpl4 = fases.get("fase_5_cpl4", {})
        stack_valor = cpl4.get("stack_valor", {})
        sumario["total_bonus"] = len([k for k in stack_valor.keys() if k.startswith("bonus_")])
        
        # Contar garantias
        garantias = cpl4.get("garantias_agressivas", [])
        sumario["total_garantias"] = len(garantias) if isinstance(garantias, list) else 0
        
        # Avaliar complexidade
        total_elementos = (
            len(fases.get("fase_2_cpl1", {}).get("teasers", [])) +
            len(fases.get("fase_3_cpl2", {}).get("casos_sucesso_detalhados", [])) +
            len(fases.get("fase_4_cpl3", {}).get("estrutura_passo_passo", [])) +
            sumario["total_bonus"]
        )
        
        if total_elementos > 20:
            sumario["nivel_complexidade"] = "Alto"
        elif total_elementos < 10:
            sumario["nivel_complexidade"] = "Baixo"
        
        logger.info("✅ Sumário executivo gerado")
        return sumario
        
    except Exception as e:
        logger.error(f"❌ Erro ao gerar sumário executivo: {str(e)}")
        return {
            "titulo_protocolo": "Erro na geração",
            "total_fases": 0,
            "estrategia_principal": "Não especificada",
            "erro": str(e)
        }


# Função principal para executar todo o fluxo de criação do CPL
async def executar_fluxo_completo_cpl(
    session_id: str,
    sintese_master: Dict[str, Any],
    avatar_data: Dict[str, Any],
    contexto_estrategico: Dict[str, Any],
    dados_web: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Executa o fluxo completo de criação do módulo CPL
    
    Args:
        session_id: ID da sessão
        sintese_master: Síntese completa da análise
        avatar_data: Dados do avatar gerado
        contexto_estrategico: Contexto estratégico definido
        dados_web: Dados brutos da pesquisa web
        
    Returns:
        Dict com resultado completo do fluxo CPL
    """
    try:
        logger.info("🚀 Iniciando fluxo completo de criação do módulo CPL")
        
        # 1. Gerar o módulo CPL
        modulo_cpl = await generate_cpl_module(
            session_id=session_id,
            sintese_master=sintese_master,
            avatar_data=avatar_data,
            contexto_estrategico=contexto_estrategico,
            dados_web=dados_web
        )
        
        # 2. Validar estrutura
        estrutura_valida = validar_estrutura_cpl(modulo_cpl)
        
        # 3. Gerar sumário executivo
        sumario = gerar_sumario_executivo(modulo_cpl)
        
        # 4. Compilar resultado final
        resultado_final = {
            "modulo_cpl": modulo_cpl,
            "validacao": {
                "estrutura_valida": estrutura_valida,
                "timestamp_geracao": datetime.now().isoformat(),
                "session_id": session_id
            },
            "sumario_executivo": sumario,
            "metadados": {
                "versao_sistema": "ARQV30 Enhanced v3.0",
                "modulo": "CPL Creator",
                "total_fases_geradas": len(modulo_cpl.get("fases", {})),
                "contexto_utilizado": {
                    "sintese_master": bool(sintese_master),
                    "avatar_data": bool(avatar_data),
                    "contexto_estrategico": bool(contexto_estrategico),
                    "dados_web": bool(dados_web)
                }
            }
        }
        
        # 5. Salvar resultado final
        salvar_etapa("fluxo_cpl_completo", resultado_final, categoria="modulos_principais", session_id=session_id)
        
        logger.info("✅ Fluxo completo de CPL executado com sucesso")
        return resultado_final
        
    except Exception as e:
        logger.error(f"❌ Erro no fluxo completo de CPL: {str(e)}")
        return {
            "modulo_cpl": {},
            "validacao": {
                "estrutura_valida": False,
                "erro": str(e),
                "timestamp_geracao": datetime.now().isoformat(),
                "session_id": session_id
            },
            "sumario_executivo": {"erro": str(e)},
            "metadados": {
                "versao_sistema": "ARQV30 Enhanced v3.0",
                "modulo": "CPL Creator",
                "status": "erro"
            }
        }
