#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v3.0 - Viral Content Analyzer
Analisa conteúdo viral e captura screenshots específicas
"""

import os
import logging
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
import time
import json

logger = logging.getLogger(__name__)

class ViralContentAnalyzer:
    """Analisa conteúdo viral e captura screenshots específicas"""

    def __init__(self):
        """Inicializa o analisador de conteúdo viral"""
        self.enabled = True
        logger.info("📊 Viral Content Analyzer inicializado")

    async def analyze_viral_content(
        self,
        search_query: str, # Query de busca usada anteriormente
        session_id: str,
        max_captures: int = 15 # Número máximo de capturas
    ) -> Dict[str, Any]:
        """
        Analisa conteúdo viral identificado nas etapas anteriores e captura screenshots.

        Args:
            search_query: A query de busca usada.
            session_id: ID da sessão.
            max_captures: Número máximo de screenshots para capturar.

        Returns:
            Dict contendo conteúdo viral identificado e screenshots capturados.
        """
        logger.info(f"🔍 Iniciando análise de conteúdo viral para sessão: {session_id}")

        try:
            # 1. Garantir que o diretório da sessão exista antes de salvar qualquer coisa
            session_dir = f"analyses_data/{session_id}"
            os.makedirs(session_dir, exist_ok=True)
            logger.debug(f"📂 Diretório da sessão garantido: {session_dir}")

            # 2. Carregar os resultados da pesquisa social/viral da sessão
            # Assume-se que os resultados foram salvos em um arquivo específico pela Etapa 1
            social_data_file = f"analyses_data/{session_id}/dados_pesquisa_web.json"
            social_results_data = {}
            if os.path.exists(social_data_file):
                try:
                    with open(social_data_file, 'r', encoding='utf-8') as f:
                        social_results_data = json.load(f)
                    logger.debug(f"📂 Dados sociais carregados de {social_data_file}")
                except Exception as e:
                    logger.error(f"❌ Erro ao carregar dados sociais: {e}")

            # Extrair resultados sociais do dicionário carregado
            all_social_results = social_results_data.get('social_results', [])
            youtube_results = social_results_data.get('youtube_results', [])

            # Combinar resultados sociais e do YouTube para análise
            combined_social_results = all_social_results + youtube_results
            logger.info(f"🔗 Combinando {len(all_social_results)} resultados sociais e {len(youtube_results)} resultados do YouTube para análise.")

            # 3. Identificar conteúdo viral com base nos scores existentes
            viral_content_identified = self._identify_viral_content(combined_social_results)
            logger.info(f"🔥 {len(viral_content_identified)} conteúdos virais identificados para captura.")

            # 4. Capturar screenshots dos conteúdos virais identificados
            screenshots_captured = await self._capture_viral_screenshots(viral_content_identified, session_id, max_captures)
            logger.info(f"📸 {len(screenshots_captured)} screenshots capturados com sucesso.")

            # 5. Compilar e retornar o resultado
            analysis_result = {
                "session_id": session_id,
                "search_query": search_query,
                "analysis_timestamp": datetime.now().isoformat(),
                "viral_content_identified": viral_content_identified,
                "screenshots_captured": screenshots_captured,
                "summary": {
                    "total_social_items_analyzed": len(combined_social_results),
                    "viral_content_found": len(viral_content_identified),
                    "screenshots_taken": len(screenshots_captured)
                }
            }

            # 6. Salvar um resumo da análise em um arquivo para referência futura
            # Agora que o diretório está garantido, esta operação não deve falhar por causa do diretório
            analysis_summary_path = f"analyses_data/{session_id}/analise_viral_resumo.json"
            try:
                with open(analysis_summary_path, 'w', encoding='utf-8') as f:
                    json.dump(analysis_result, f, ensure_ascii=False, indent=2)
                logger.info(f"💾 Resumo da análise viral salvo em: {analysis_summary_path}")
            except Exception as e:
                logger.error(f"❌ Erro ao salvar resumo da análise viral: {e}")
                # Mesmo que o salvamento falhe, continuamos com o resultado em memória

            return analysis_result

        except Exception as e:
            logger.error(f"❌ Erro crítico na análise de conteúdo viral: {e}", exc_info=True)
            # Retorna um dicionário de erro estruturado
            error_result = {
                "session_id": session_id,
                "search_query": search_query,
                "analysis_timestamp": datetime.now().isoformat(),
                "viral_content_identified": [],
                "screenshots_captured": [],
                "summary": {
                    "total_social_items_analyzed": 0,
                    "viral_content_found": 0,
                    "screenshots_taken": 0,
                    "critical_error": str(e)
                },
                "error": True,
                "error_message": str(e)
            }
            
            # Tenta salvar o erro também, garantindo o diretório
            session_dir = f"analyses_data/{session_id}"
            os.makedirs(session_dir, exist_ok=True)
            error_file_path = f"{session_dir}/analise_viral_erro.json"
            try:
                with open(error_file_path, 'w', encoding='utf-8') as f:
                    json.dump(error_result, f, ensure_ascii=False, indent=2)
                logger.info(f"💾 Erro da análise viral salvo em: {error_file_path}")
            except Exception as save_error:
                logger.error(f"❌ Erro ao salvar log de erro da análise viral: {save_error}")

            # Re-levanta o erro para que o workflow possa decidir como proceder
            # (por exemplo, marcando a etapa como falha)
            raise # <<< CRÍTICO: Re-levanta o erro


    def _identify_viral_content(self, all_social_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identifica conteúdo viral para captura de screenshots"""
        if not all_social_results:
            logger.warning("⚠️ Nenhum resultado social fornecido para identificação viral.")
            return []

        # Ordena por score viral (assumindo que 'viral_score' ou 'engagement_rate' exista)
        # Tenta 'viral_score' primeiro, depois 'engagement_rate'
        def sort_key(item):
            # Converte para float com segurança
            try:
                return float(item.get('viral_score', item.get('engagement_rate', 0)))
            except (ValueError, TypeError):
                return 0.0

        sorted_content = sorted(
            all_social_results,
            key=sort_key,
            reverse=True
        )

        # Seleciona top 20 conteúdos virais para ter opções
        viral_content = []
        seen_urls = set()

        for content in sorted_content:
            url = content.get('url', '')
            # Adiciona verificação para evitar duplicatas e conteúdo sem URL
            if url and url not in seen_urls and len(viral_content) < 20:
                viral_content.append(content)
                seen_urls.add(url)

        logger.info(f"🔥 {len(viral_content)} conteúdos virais identificados (top 20 por score)")
        return viral_content

    async def _capture_viral_screenshots(
        self,
        viral_content: List[Dict[str, Any]],
        session_id: str,
        max_captures: int
    ) -> List[Dict[str, Any]]:
        """Captura screenshots específicas do conteúdo viral"""
        screenshots = []

        if not viral_content:
             logger.info("📭 Nenhum conteúdo viral para capturar screenshots.")
             return screenshots

        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from webdriver_manager.chrome import ChromeDriverManager

            # Configura Chrome em modo headless
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-gpu")
            # chrome_options.add_argument("--force-device-scale-factor=1") # Pode ajudar com qualidade

            service = Service(ChromeDriverManager().install())
            # Aumenta o tempo limite implícito
            driver = webdriver.Chrome(service=service, options=chrome_options)

            # Cria diretório para screenshots - Garantido no caller, mas reforçado aqui
            screenshots_dir = f"analyses_data/files/{session_id}"
            os.makedirs(screenshots_dir, exist_ok=True)

            try:
                for i, content in enumerate(viral_content, 1):
                    if len(screenshots) >= max_captures:
                        logger.info(f"🛑 Limite máximo de capturas ({max_captures}) atingido.")
                        break

                    try:
                        url = content.get('url', '')
                        platform = content.get('platform', 'web').lower()
                        title = content.get('title', f'Conteúdo Viral {i}')

                        if not url:
                            logger.warning(f"⚠️ Conteúdo {i} sem URL, pulando captura.")
                            continue

                        logger.info(f"📸 Tentando captura {len(screenshots)+1}/{max_captures}: {title[:50]}... ({platform})")

                        # Verifica se é um post do Facebook ou Instagram para tentar captura expandida
                        expanded_success = False
                        if 'facebook' in platform or 'instagram' in platform:
                            try:
                                logger.debug(f"🔍 Tentando captura expandida para {platform}...")
                                expanded_success = await self._attempt_expanded_view_capture(driver, url, platform, i, screenshots_dir, content, screenshots, session_id)
                                logger.debug(f"🔍 Captura expandida para {platform} {'bem-sucedida' if expanded_success else 'falhou'}.")
                            except Exception as e:
                                logger.warning(f"⚠️ Erro na tentativa expandida para {platform} ({url}): {e}. Tentando captura normal.")

                        # Se a captura expandida falhar ou não for aplicável, faz a captura normal da página
                        if not expanded_success:
                             logger.debug(f"📄 Fazendo captura normal da página para {url}...")
                             success = await self._attempt_normal_page_capture(driver, url, platform, i, screenshots_dir, content, screenshots, session_id)
                             if success:
                                 logger.info(f"✅ Captura normal bem-sucedida para {url}")
                             else:
                                 logger.warning(f"⚠️ Falha na captura normal para {url}")

                    except Exception as e:
                        logger.error(f"❌ Erro ao processar conteúdo {i} para captura ({content.get('url', 'N/A')}): {e}")

            finally:
                driver.quit()
                logger.debug("🏁 WebDriver encerrado.")

        except ImportError:
            logger.error("❌ Selenium não instalado - screenshots não disponíveis")
            # Salva um arquivo de erro ou avisa de outra forma?
        except Exception as e:
            logger.error(f"❌ Erro crítico na captura de screenshots: {e}", exc_info=True)

        logger.info(f"🏁 Processo de captura concluído. Total de screenshots salvos: {len(screenshots)}")
        return screenshots

    async def _attempt_expanded_view_capture(self, driver, url: str, platform: str, index: int, screenshots_dir: str, content: Dict, screenshots_list: List, session_id: str) -> bool:
        """
        Tenta capturar uma imagem em modo de visualização expandida (para Facebook/Instagram).
        Retorna True se a captura foi bem-sucedida, False caso contrário.
        """
        try:
            # Acessa a URL do post
            driver.get(url)
            logger.debug(f"🌐 Navegando para {url}")

            # Aguarda carregamento inicial
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(3) # Tempo extra para renderização

            # Tenta encontrar e clicar em botões para expandir a visualização
            clicked = False
            if 'instagram' in platform:
                # Procura por botões específicos do Instagram para ver foto
                # Seletor comum para o botão de expandir foto no Instagram
                expand_selectors = [
                     "button[aria-label='Ver foto']", # Português
                     "button[aria-label='View photo']", # Inglês
                     "button svg[aria-label='Ver foto']", # Às vezes o SVG tem o aria-label
                     "button svg[aria-label='View photo']",
                     # Seletor alternativo baseado em classes (pode mudar)
                     "div[role='button'] > div > div[style*='background-image']" # Foto em destaque
                ]
                for selector in expand_selectors:
                    try:
                        button = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                        button.click()
                        logger.debug(f"👆 Clicado no botão de expansão (seletor: {selector})")
                        clicked = True
                        break # Sai do loop se encontrar e clicar
                    except:
                         continue # Tenta o próximo seletor
            elif 'facebook' in platform:
                 # Procura por botões específicos do Facebook
                 # Seletor para fotos em posts do Facebook
                 expand_selectors = [
                     "div[role='main'] div[data-sigil='mfeed_pivots_message feed-story-highlight-candidate'] div[data-sigil='mfeed_pivots_message feed-story-highlight-candidate'] img", # Foto principal (muito específico)
                     # Um seletor mais genérico para imagem dentro de um post
                     "div[data-pagelet='Feed'] div[data-ad-preview='message'] img", # Tentativa
                     # Às vezes é um link para a foto em tamanho maior
                     "a[href*='/photo.php'] img", # Link para foto
                     "a[href*='/photos/'] img" # Outro formato de link
                 ]
                 for selector in expand_selectors:
                     try:
                         # Para Facebook, muitas vezes clicar na imagem a expande
                         img_element = WebDriverWait(driver, 5).until(
                             EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                         )
                         img_element.click()
                         logger.debug(f"👆 Clicado na imagem para expansão (seletor: {selector})")
                         clicked = True
                         # Após clicar, espera um modal ou nova página
                         time.sleep(2)
                         break
                     except:
                          continue

            # Se clicou em algo para expandir, espera a nova imagem carregar
            if clicked:
                 try:
                     # Espera por uma nova imagem carregada (modal, lightbox etc.)
                     # Este seletor é genérico, pode precisar de ajuste
                     WebDriverWait(driver, 10).until(
                         EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog'] img, div[class*='Modal'] img, img[src*='fbcdn'], img[src*='instagram']"))
                     )
                     logger.debug("🖼️ Nova imagem expandida detectada.")
                     time.sleep(2) # Tempo extra para garantir carregamento
                 except:
                      logger.debug("⏳ Timeout esperando nova imagem expandida, continuando com a captura atual.")

            # Captura a screenshot da tela (que deve estar com a imagem expandida)
            filename = f"viral_post_{index:02d}.png"
            screenshot_path = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(screenshot_path)
            logger.debug(f"💾 Screenshot salvo em {screenshot_path}")

            # Verifica se foi criado e tem conteúdo
            if os.path.exists(screenshot_path) and os.path.getsize(screenshot_path) > 1024: # > 1KB
                relative_path = f"files/{session_id}/{filename}"
                screenshots_list.append({
                    'content_data': content,
                    'screenshot_path': screenshot_path,
                    'relative_path': relative_path, # Caminho relativo para uso no markdown
                    'filename': filename,
                    'url': url,
                    'title': content.get('title', ''),
                    'platform': platform,
                    'viral_score': content.get('viral_score', content.get('engagement_rate', 0)),
                    'captured_at': datetime.now().isoformat(),
                    'capture_method': 'expanded_view'
                })
                return True
            else:
                # Se o arquivo estiver vazio ou muito pequeno, remove
                if os.path.exists(screenshot_path):
                    os.remove(screenshot_path)
                logger.warning(f"⚠️ Screenshot expandido resultou em arquivo inválido: {screenshot_path}")
                return False

        except Exception as e:
             logger.warning(f"⚠️ Erro na captura expandida para {url}: {e}")
             return False # Falha na captura expandida

    async def _attempt_normal_page_capture(self, driver, url: str, platform: str, index: int, screenshots_dir: str, content: Dict, screenshots_list: List, session_id: str) -> bool:
        """
        Faz a captura normal da página inteira.
        Retorna True se a captura foi bem-sucedida, False caso contrário.
        """
        try:
            # Acessa a URL
            driver.get(url)
            logger.debug(f"🌐 Navegando para {url}")

            # Aguarda carregamento
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            # Aguarda renderização completa
            time.sleep(3)

            # Captura screenshot
            filename = f"viral_web_{index:02d}.png"
            screenshot_path = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(screenshot_path)
            logger.debug(f"💾 Screenshot normal salvo em {screenshot_path}")

            # Verifica se foi criado e tem conteúdo
            if os.path.exists(screenshot_path) and os.path.getsize(screenshot_path) > 1024: # > 1KB
                relative_path = f"files/{session_id}/{filename}"
                screenshots_list.append({
                    'content_data': content,
                    'screenshot_path': screenshot_path,
                    'relative_path': relative_path, # Caminho relativo para uso no markdown
                    'filename': filename,
                    'url': url,
                    'title': content.get('title', ''),
                    'platform': platform,
                    'viral_score': content.get('viral_score', content.get('engagement_rate', 0)),
                    'captured_at': datetime.now().isoformat(),
                    'capture_method': 'full_page'
                })
                return True
            else:
                # Se o arquivo estiver vazio ou muito pequeno, remove
                if os.path.exists(screenshot_path):
                    os.remove(screenshot_path)
                logger.warning(f"⚠️ Screenshot normal resultou em arquivo inválido: {screenshot_path}")
                return False

        except Exception as e:
             logger.error(f"❌ Erro na captura normal para {url}: {e}")
             return False # Falha na captura normal


# Instância global
viral_content_analyzer = ViralContentAnalyzer()
