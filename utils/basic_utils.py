from termcolor import colored


def resetter(metric_objects):
    metric_objects['train_loss'].reset_states()
    metric_objects['train_acc'].reset_states()
    metric_objects['validation_loss'].reset_states()
    metric_objects['validation_acc'].reset_states()


def training_reporter(epoch, losses_accs, metric_objects, exp_name=None):
    train_loss = metric_objects['train_loss']
    train_acc = metric_objects['train_acc']
    validation_loss = metric_objects['validation_loss']
    validation_acc = metric_objects['validation_acc']

    losses_accs['train_losses'].append(train_loss.result().numpy())
    losses_accs['train_accs'].append(train_acc.result().numpy())
    losses_accs['validation_losses'].append(validation_loss.result().numpy())
    losses_accs['validation_accs'].append(validation_acc.result().numpy())

    if exp_name:
        print(colored('Exp: ', 'red', 'on_white'), exp_name)
    print(colored('Epoch: ', 'red'), epoch)

    template = 'Train Loss: {:.4f}\t Train Accuracy: {:.2f}% \n' + \
        'Validation Loss: {:.4f}\t Validation Accuracy: {:.2f}% \n'
    print(template.format(losses_accs['train_losses'][-1],
                          losses_accs['train_accs'][-1],
                          losses_accs['validation_losses'][-1],
                          losses_accs['validation_accs'][-1]))