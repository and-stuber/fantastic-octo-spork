import torch
import torch.nn as nn
import torch.optim as optim
import tensorflow as tf
from torchvision import datasets, transforms

# Hiperparâmetros
batch_size = 64
image_size = 28
nz = 100  # Dimensão do vetor de entrada para o gerador (noise vector)
ngf = 64  # Tamanho dos feature maps no gerador
ndf = 64  # Tamanho dos feature maps no discriminador
num_epochs = 100
lr = 0.0002
beta1 = 0.5

# Transformação dos dados
transform = transforms.Compose([
    transforms.Resize(image_size),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Carregar o conjunto de dados MNIST
mnist = tf.keras.datasets.mnist

# Dataset e DataLoader
# Original -> dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)

dataset = mnist
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Definição do Gerador
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            nn.ConvTranspose2d(nz, ngf * 4, 4, 1, 0, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 4, ngf * 2, 3, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf * 2, ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            nn.ConvTranspose2d(ngf, 1, 4, 2, 1, bias=False),
            nn.Tanh()
        )

    def forward(self, input):
        return self.main(input)

# Definição do Discriminador
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.main = nn.Sequential(
            nn.Conv2d(1, ndf, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 2, ndf * 4, 3, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(ndf * 4, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.main(input)

# Instanciamento dos modelos
netG = Generator().cuda()
netD = Discriminator().cuda()

# Função de perda e otimizadores
criterion = nn.BCELoss()
optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(beta1, 0.999))
optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(beta1, 0.999))

# Função para treinar os modelos
def train():
    for epoch in range(num_epochs):
        for i, data in enumerate(dataloader, 0):
            # Treinamento do Discriminador
            netD.zero_grad()
            real_cpu = data[0].cuda()
            batch_size = real_cpu.size(0)
            label = torch.full((batch_size,), 1, dtype=torch.float, device='cuda')
            output = netD(real_cpu).view(-1)
            errD_real = criterion(output, label)
            errD_real.backward()
            noise = torch.randn(batch_size, nz, 1, 1, device='cuda')
            fake = netG(noise)
            label.fill_(0)
            output = netD(fake.detach()).view(-1)
            errD_fake = criterion(output, label)
            errD_fake.backward()
            errD = errD_real + errD_fake
            optimizerD.step()

            # Treinamento do Gerador
            netG.zero_grad()
            label.fill_(1)
            output = netD(fake).view(-1)
            errG = criterion(output, label)
            errG.backward()
            optimizerG.step()

        print(f'Epoch [{epoch+1}/{num_epochs}] Loss_D: {errD.item()}, Loss_G: {errG.item()}')

        # Salvar algumas imagens geradas a cada poucos epochs
        if epoch % 10 == 0:
            with torch.no_grad():
                fake = netG(noise).detach().cpu()
            save_image(fake, f'output_{epoch}.png', normalize=True)

if __name__ == "__main__":
    train()
