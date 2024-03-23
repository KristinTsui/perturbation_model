import torch

from scgpt.features.Perturbation_Prediction import (
    pad_token,
    special_tokens,
    pad_value,
    pert_pad_id,
    n_hvg,
    include_zero_gene,
    max_seq_len,
    MLM,
    CLS,
    CCE,
    MVC,
    ECS,
    cell_emb_style,
    mvc_decoder_style,
    amp,
    load_model,
    load_param_prefixs,
    lr,
    batch_size,
    eval_batch_size,
    epochs,
    schedule_interval,
    early_stop,
    embsize,
    d_hid,
    nlayers,
    nhead,
    n_layers_cls,
    dropout,
    use_fast_transformer,
    log_interval,
    data_name,
    split,
    perts_to_plot,
    device,
)


def test_settings():
    assert pad_token == "<pad>"
    assert special_tokens == ["<pad>", "<cls>", "<eoc>"]
    assert pad_value == 0
    assert pert_pad_id == 2
    assert n_hvg == 0
    assert include_zero_gene == "all"
    assert max_seq_len == 1536
    assert MLM is True
    assert CLS is False
    assert CCE is False
    assert MVC is False
    assert ECS is False
    assert cell_emb_style == "cls"
    assert mvc_decoder_style == "inner product, detach"
    assert amp is True
    assert load_model == "../finetuned_model"
    assert load_param_prefixs == ["encoder", "value_encoder", "transformer_encoder"]
    assert lr == 1e-4
    assert batch_size == 16
    assert eval_batch_size == 16
    assert epochs == 1
    assert schedule_interval == 1
    assert early_stop == 5
    assert embsize == 512
    assert d_hid == 512
    assert nlayers == 12
    assert nhead == 8
    assert n_layers_cls == 3
    assert dropout == 0.2
    assert use_fast_transformer is True
    assert log_interval == 100
    assert data_name == "adamson"
    assert split == "simulation"
    assert perts_to_plot == ["KCTD16+ctrl"]
    assert device == torch.device("cuda" if torch.cuda.is_available() else "cpu")