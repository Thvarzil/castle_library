FROM node:16-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy all files
COPY . .

# Expose port (default for React)
EXPOSE 3000

# Start the app
CMD ["npm", "start"]