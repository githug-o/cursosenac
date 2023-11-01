<html>
    <head>
    <title>ViaCEP Webservice</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <!-- Adicionando Javascript -->
    <script>
    
    function limpa_formulário_cep() {
            //Limpa valores do formulário de cep.
            document.getElementById('rua').value=("");
            document.getElementById('bairro').value=("");
            document.getElementById('cidade').value=("");
            document.getElementById('uf').value=("");
            document.getElementById('ibge').value=("");
    }

    function meu_callback(conteudo) {
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('rua').value=(conteudo.logradouro);
            document.getElementById('bairro').value=(conteudo.bairro);
            document.getElementById('cidade').value=(conteudo.localidade);
            document.getElementById('uf').value=(conteudo.uf);
            document.getElementById('ibge').value=(conteudo.ibge);
        } //end if.
        else {
            //CEP não Encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
        }
    }
        
    function pesquisacep(valor) {

        //Nova variável "cep" somente com dígitos.
        var cep = valor.replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                document.getElementById('rua').value="...";
                document.getElementById('bairro').value="...";
                document.getElementById('cidade').value="...";
                document.getElementById('uf').value="...";
                document.getElementById('ibge').value="...";

                //Cria um elemento javascript.
                var script = document.createElement('script');

                //Sincroniza com o callback.
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

                //Insere script no documento e carrega o conteúdo.
                document.body.appendChild(script);

            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    };

    </script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>

    <body>
    <!-- Inicio do formulario -->
      <form method="post" action="{{route('update', $cliente[0]->id)}}">
        @csrf
        <label class="form-label">Nome:
        <input class="form-control" name="nome" value="{{$cliente[0]->nome}}" type="text" id="nome" size="60" /></label><br />
        <label class="form-label">E-mail:
        <input class="form-control" name="email" value="{{$cliente[0]->email}}" type="text" id="email" size="60" /></label><br />
        <label class="form-label" class="form-label">Telefone:
        <input class="form-control" name="telefone" value="{{$cliente[0]->telefone}}" type="text" id="telefone" size="60" /></label><br />
        <br>
        <label class="form-label">CEP:
        <input class="form-control" name="cep" value="{{$cliente[0]->cep}}" type="text" id="cep" value="" size="10" maxlength="9"
               onblur="pesquisacep(this.value);" /></label><br />
        <label class="form-label">Rua:
        <input class="form-control" name="rua" value="{{$cliente[0]->rua}}" type="text" id="rua" size="60" /></label><br />
        <label class="form-label">Bairro:
        <input class="form-control" name="bairro" value="{{$cliente[0]->bairro}}" type="text" id="bairro" size="40" /></label><br />
        <label class="form-label">Cidade:
        <input class="form-control" name="cidade" value="{{$cliente[0]->cidade}}" type="text" id="cidade" size="40" /></label><br />
        <label class="form-label">Estado:
        <input class="form-control" name="uf" value="{{$cliente[0]->uf}}" type="text" id="uf" size="2" /></label><br />
        <label class="form-label">Número:
        <input class="form-control" name="numero" value="{{$cliente[0]->numero}}" type="text" id="numero" size="8" /></label><br />
        <label class="form-label">Complemento:
        <input class="form-control" name="complemento" value="{{$cliente[0]->complemento}}" type="text" id="complemento" size="8" /></label><br />
        <input name="ibge" type="hidden" id="ibge" size="8" />
        <div>
            <button type="submit" class="btn btn-primary">Salvar</button>
            <a href="{{route('index')}}"><button type="button" class="btn btn-warning">Voltar</button>
        </div>

      </form>
    </body>

    </html>